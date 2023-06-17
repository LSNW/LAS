from pydub import AudioSegment
from zipfile import ZipFile
import zipfile, os, zlib, re
from django.core.exceptions import ValidationError


def contained(times, avfile, extension):
    if extension == 'wav':
        audio = AudioSegment.from_wav(avfile)
    else:
        audio = AudioSegment.from_mp3(avfile)
    full_end = audio.duration_seconds * 1000
    return max(times) < full_end

def convertToMS (timestamp):
    inf = timestamp.split(':')
    if len(inf) == 3:
        hour = int(re.search(r'\d+', inf[0]).group())
        minute = int(re.search(r'\d+', inf[1]).group())
        second = int(re.search(r'\d+', inf[2]).group())

        return (hour * 3600 + minute * 60 + second) * 1000
    elif len(inf) == 2:
        minute = int(re.search(r'\d+', inf[0]).group())
        second = int(re.search(r'\d+', inf[1]).group())

        return (minute * 60 + second) * 1000
    else:
        raise Error()


def convertToMinSec (timems):
    totalSec = timems / 1000
    mins = int(totalSec // 60)
    sec = int(totalSec % 60)
    return str(mins) + ":" + str(sec)


def processTimestamps(timestamps):
    if ('/' in timestamps) or ('\\' in timestamps):
        raise ValidationError({'timestamps': ['Invalid characters (slashes)',]})

    try:
        stamps = re.split('\r|\n', timestamps)
        stamps = list(filter(lambda x: x != '', stamps))
        numTracks = len(stamps)
        times = []
        titles = []

        for stamp in stamps:
            description = stamp.split(' ', 1)
            times.append(description[0])
            titles.append(description[1])
        return [convertToMS(time) for time in times], titles

    except:
        raise ValidationError({'timestamps': ['Improperly formatted timestamps',]})



def trimMP3(audio_file, listOfTimestamps, titles, tag): 
    audio = AudioSegment.from_file(os.path.join('media', 'uploads', audio_file), format='mp3')
    full_end = audio.duration_seconds * 1000
    
    listOfTimestamps.append(full_end)

    zip = ZipFile(os.path.join('media', 'tempzips','SS-' + tag + '.zip'), 'w', zipfile.ZIP_DEFLATED)

    start = listOfTimestamps[0]

    for i,t in enumerate(listOfTimestamps[1:]):
        end = t
        snippet = audio[start:end]
        filename = os.path.join("media", "avfiles", titles[i] + ".mp3")
        s = snippet.export(filename, format = "mp3")
        zip.write(filename, arcname=titles[i]+".mp3")
        s.close()
        os.remove(os.path.join("media", "avfiles", titles[i] + ".mp3"))
        start = end
    

    zip.close()

def trimWAV(audio_file, listOfTimestamps, titles, tag): 
    audio = AudioSegment.from_wav(audio_file)
    full_end = audio.duration_seconds * 1000
    
    listOfTimestamps.append(full_end)

    zip = ZipFile(os.path.join('media', 'tempzips','SS-' + tag + '.zip'), 'w', zipfile.ZIP_DEFLATED)

    start = listOfTimestamps[0]

    for i,t in enumerate(listOfTimestamps[1:]):
        end = t
        snippet = audio[start:end]
        filename = os.path.join("media", "avfiles", titles[i] + ".wav")
        s = snippet.export(filename, format = "wav")
        zip.write(filename, arcname=titles[i]+".wav")
        s.close()
        os.remove(os.path.join("media", "avfiles", titles[i] + ".wav"))
        start = end
    

    zip.close()