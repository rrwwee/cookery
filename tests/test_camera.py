"""Check the capture loop with substitutes for the two macOS commands."""
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/cookery/skills/cook/scripts/camera.sh'


class CameraTests(unittest.TestCase):
    def test_loop_writes_pictures_and_latest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bin_dir = root/'bin'; bin_dir.mkdir()
            (bin_dir/'osascript').write_text('#!/bin/sh\ncat >/dev/null\necho 123\n')
            (bin_dir/'screencapture').write_text('#!/bin/sh\nfor output do :; done\nprintf "test picture" > "$output"\n')
            for command in bin_dir.iterdir(): command.chmod(0o755)
            env = dict(os.environ, PATH=str(bin_dir)+':'+os.environ['PATH'])
            folder = root/'pictures with spaces'
            process = subprocess.Popen(['/bin/sh', str(SCRIPT), str(folder)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                deadline = time.monotonic()+8
                while len(list(folder.glob('[0-9]*.jpg'))) < 2 and time.monotonic() < deadline:
                    time.sleep(.05)
                frames = sorted(folder.glob('[0-9]*.jpg'))
                self.assertEqual(len(frames), 2)
                self.assertEqual((folder/'latest.jpg').read_bytes(), b'test picture')
                self.assertGreaterEqual(frames[1].stat().st_mtime-frames[0].stat().st_mtime, 4.5)
            finally:
                process.terminate(); process.communicate(timeout=7)

    def test_missing_preview_stops_before_capture(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = root/'osascript'; command.write_text('#!/bin/sh\ncat >/dev/null\nexit 1\n'); command.chmod(0o755)
            env = dict(os.environ, PATH=str(root)+':'+os.environ['PATH'])
            folder = root/'pictures'
            result = subprocess.run(['/bin/sh', str(SCRIPT), str(folder)], env=env, capture_output=True, timeout=3)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((folder/'latest.jpg').exists())


if __name__ == '__main__': unittest.main(verbosity=2)
