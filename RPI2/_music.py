from audioplayer import AudioPlayer
import alsaaudio

class Music():
	def __init__(self):
		self.tracks = {} # 'track': (state, AudioPlayer())
		self.mix = alsaaudio.Mixer()

	def change_volume(self, vol):
		self.mix.setvolume(vol)

	def play(self, track):
		if self.tracks.get(track):
			if not self.tracks[track][0]:
				self.tracks[track][0] = True
				self.tracks[track][1].resume()
			else:
				self.tracks[track][1].play()
		else:
			self.tracks[track] = (True, AudioPlayer(f'/home/user/Desktop/RPI2/mp3/{track}.mp3'))
			self.tracks[track][1].play()

	def stop(self, track):
		if self.tracks.get(track):
			self.tracks[track][1].stop()
			del self.tracks[track]

	def pause(self, track):
		if self.tracks.get(track):
			self.tracks[track][0] = False
			self.tracks[track][1].pause()
