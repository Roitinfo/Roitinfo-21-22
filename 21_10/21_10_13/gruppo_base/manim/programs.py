from manim import *
from math import *

class inizio(Scene):
	def construct(self):
		obj = Code("code/prova.cpp", style=Code.styles_list[13])
		s = SurroundingRectangle(obj)
		self.play(Write(obj), run_time=0.3)
		for line in obj.code:
			print(line)
			if len(line.submobjects) > 1:
				self.play(FadeOut(line))
