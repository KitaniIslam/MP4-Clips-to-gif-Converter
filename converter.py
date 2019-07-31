import imageio
import os

clip = os.path.abspath('champe.MP4')
print(clip)


def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    # read the content of the clip.
    frames = imageio.get_reader(inputPath)

    # get the FPS from the Clip to generate Gif with the same FPS value.
    fps = frames.get_meta_data()['fps']

    # the new Clip configuration.
    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in frames:
        writer.append_data(frame)
        print(f'Fram : {frame}')
    writer.close()


gifMaker(clip, '.gif')
