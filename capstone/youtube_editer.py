import os
import pandas as pd
from pytube import YouTube
from moviepy.editor import *


# Step 1: Download File (Done)
# Step 2: Assign Meta data to accompany it (per URL) (Done)
# Step 3: Splice footage (Done)

def clean_title(title_input):
    bad_chars = [';', ' ', ':', '*', '1', "'", '"', ',', '.', '?', '&', '@', '#', '/', '\\', '|', '-']
    for i in bad_chars:
        title_input = title_input.replace(i, '')
    return title_input


def clean_couplets(couplet_series):
    for couplet_group in range(0, len(couplet_series)):
        couplet_series[couplet_group] = couplet_series[couplet_group].replace('/', ',').split(',')
        for couplet in range(0, len(couplet_series[couplet_group])):
            couplet_per = couplet_series[couplet_group]
            couplet_per[couplet] = couplet_per[couplet].replace(';', ',').replace('(', '').replace(')', '').split(',')
            for time in range(0, len(couplet_per[couplet])):
                couple = couplet_per[couplet]
                couple[time] = couple[time].replace(':', ',').split(',')
                for item in range(0, len(couple[time])):
                    items = couple[time]
                    items[item] = float(items[item])
    return pd.DataFrame(couplet_series)


if __name__ == '__main__':
    df = pd.DataFrame(pd.read_csv("F:\\Springboard\\videos_to_edit.txt", header=0))
    num_urls = len(df['url'])
    download_path = "E:\\Documents\\Springboard\\videos"
    # Clean and store the time cut series
    couplets = df.iloc[:, 1]
    time_cuts = clean_couplets(couplets)

    print(type(df))

    # Go through every entry and make a folder, download into it, and save a text file with url
    for i in range(0, num_urls):
        # Generate YouTube Object
        yt = YouTube(df.url[i])
        # Make directory and join it
        title = clean_title(yt.title)
        unique_path = os.path.join(download_path, title)
        os.mkdir(unique_path)
        os.chdir(unique_path)
        # Download into unique folder
        out_file = yt.streams.first().download(unique_path)
        video_file = title + '.mp4'
        os.rename(out_file, video_file)
        file_name_meta = title + "_meta_" + ".txt"
        file_path = os.path.join(unique_path, file_name_meta)
        with open(file_path, "w") as file:
            file.write(yt.watch_url)
        for j in range(0, len(time_cuts.iloc[i])):
            per_url_time_cuts = time_cuts.iloc[i]
            for k in range(0, len(per_url_time_cuts[j])):
                start_time = per_url_time_cuts[j][k][0]
                end_time = per_url_time_cuts[j][k][1]
                clip_name = 'clip_' + str(k) + '.mp4'
                clip = VideoFileClip(video_file).subclip(start_time, end_time)
                video = CompositeVideoClip([clip])
                video.write_videofile(clip_name)
