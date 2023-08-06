import subprocess
import sys
from FFmpeg.ffmpeg import FFmpeg


def encode_two(camera, screen, output):
    ffmpeg = FFmpeg()
    ff = (
        ffmpeg
        .OverwriteOutput()
        .addInput(screen)
        .addInput("./logo.png")
        .addInput(camera)
        .videoCodec("libx264")
        .audioCodec("aac")
        .videoFramerate(30)
        .videoResolution(resString="1920x1080")
        .scale2refFilter(2, "0", "oh*mdar:ih*0.2", "camera", "video")  # resize camera to 20% of screen height
        .overlayFilter("video", "1", "W-w-10", "H-h-10", "v")  # overlay logo on bottom right
        .overlayFilter("v", "camera", "10", "10")  # overlay camera on top left
        .output(output)  # output file
    )
    code, stdout, stderr = ff.execute(stderr=subprocess.STDOUT, shell=False)
    print(code, stdout, stderr)


def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: python main.py <camera_file> <screen_file> <output_file>")
        return
    encode_two(args[0], args[1], args[2])


if __name__ == '__main__':
    main()
