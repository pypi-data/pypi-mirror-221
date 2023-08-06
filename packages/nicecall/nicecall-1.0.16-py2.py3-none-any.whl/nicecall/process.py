import asyncio
import nicecall
import subprocess
import threading


class Process():
    def __init__(self, args, on_stdout=None, on_stderr=None):
        self._args = args
        self._on_stdout = on_stdout
        self._on_stderr = on_stderr

    @property
    def args(self):
        return self._args

    @property
    def stream_processing_builder(self):
        return nicecall.StreamProcessingBuilder()

    def execute(self):
        with subprocess.Popen(
            self.args, universal_newlines=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as process:
            self._process_std(process)
            process.wait()
            return process.returncode

    def _process_std(self, process):
        size = (1 if self._on_stdout else 0) + (1 if self._on_stderr else 0)
        if size == 0:
            return

        # The queue is necessary to ensure stdout and stderr streams are
        # processed completely before waiting for process termination. If this
        # queue is not used, what could happen is that if Python takes too much
        # time processing lines from stdout or stderr within the threads, the
        # process will end, eventually leading to Python program stopping
        # itself and terminating the threads which were still processing
        # output.
        process_queue = asyncio.Queue(maxsize=size)

        if self._on_stdout:
            self._read_stream_async(
                process.stdout, self._on_stdout, process_queue)

        if self._on_stderr:
            self._read_stream_async(
                process.stderr, self._on_stderr, process_queue)

        while not process_queue.full():
            pass

    def on_stdout(self, action, skip_empty=False, skip_whitespace=False):
        args = locals()
        result = self._clone()
        result._on_stdout = Process._build_stream_processing(**args)
        return result

    def on_stderr(self, action, skip_empty=False, skip_whitespace=False):
        args = locals()
        result = self._clone()
        result._on_stderr = Process._build_stream_processing(**args)
        return result

    def _build_stream_processing(self, action, skip_empty, skip_whitespace):
        builder = self.stream_processing_builder
        builder.replace_action(action)

        if skip_empty:
            builder.skip_empty()

        if skip_whitespace:
            builder.skip_whitespace()

        return builder.build()

    def _clone(self):
        return Process(self.args, self._on_stdout, self._on_stderr)

    def _read_stream_async(self, stream, processing, process_queue):
        task = threading.Thread(
            target=self._read_stream, args=(stream, processing, process_queue))

        task.start()

    def _read_stream(self, stream, processing, process_queue):
        for raw_line in stream:
            line = raw_line.rstrip("\n")
            if all((prefilter(line) for prefilter in processing.filters)):
                processing.action(line)

        process_queue.put_nowait(True)
