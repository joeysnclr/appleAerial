import requests, json


def gatherFromTVOS10():
	videos = []
	i = 0

	r = requests.get('http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json')
	content = r.json()
	for item in content:
		for video in item['assets']:
			videoDict = {
				"url": video['url'],
				"location": video['accessibilityLabel'],
				"id": i
			}
			videos.append(videoDict)
			i += 1

	for v in videos:
		if v['id'] == 0:
			# if first video
			v['prev'] = len(videos) - 1
			v['next'] = v['id'] + 1
		elif v['id'] == len(videos) - 1:
			# if last video
			v['prev'] = v['id'] - 1
			v['next'] = 0
		else:
			v['prev'] = v['id'] - 1
			v['next'] = v['id'] + 1


	with open('videos.json', 'w+') as file:
		json.dump(videos, file)
			
gatherFromTVOS10()