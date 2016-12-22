import asyncio
import websockets
import json
import argparse
import urllib.request

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file', metavar='OUTPUT')
    parser.add_argument('image_file', metavar='IMAGE')
    
    return parser.parse_args()
 
async def response():
    args = parse_args()
    async with websockets.connect('ws://localhost:5672') as websocket:
        playing = False
        while True:
            answer = json.loads(await websocket.recv())
            channel = answer["channel"]
            msg = answer["payload"]
            if (channel == "playState"):
                playing = msg
                print("Playing: " + str(playing))
            if (channel == "track"):
                print("Track: " + msg['title'])
                try:
                    with open(args.output_file, 'w') as myoutput:
                        myoutput.write("%s - %s" % (msg['artist'], msg['title']))
                    urllib.request.urlretrieve(msg['albumArt'] , args.image_file)  
                except FileNotFoundError as e:
                    print("Couldn't find file '%s'" % e)

asyncio.get_event_loop().run_until_complete(response())
