from manim import *

class Easy2(Scene):
	def construct(self):
		arr = []
		with open("input/input2.txt") as file:
			lines = file.readlines()
			n = int(lines[0].split()[0])
			for line in lines[1:n+1]:
				arr.append(list(map(int, line.split())))

		minX = -5
		step = 2 
		size = step * 0.8

		pairs = []
		idxs = []
		lines = []

		for i, pair in enumerate(arr):
			x = minX + step * (i)

			line = Line([x, 3.5, 0], [x, -0.5, 0]);

			idx = Tex(str(i)).scale(size).move_to([x + step/2, 3, 0]).set_fill(color = YELLOW)
			first = Tex(str(pair[0])).scale(size).move_to([x + step/2, 2, 0])
			second = Tex(str(pair[1])).scale(size).move_to([x + step/2, 1, 0])

			pairs.append([first, second])
			idxs.append(idx)
			lines.append(line)

		anim = []
		for line in lines:
			anim.append(Create(line))

		self.play(Create(Line([-7, 0.5, 0], [7, 0.5, 0])), Create(Line([-7, 2.5, 0], [7, 2.5, 0])), run_time = 0.4)
		self.play(*anim, run_time = 0.4)
		
		anim = []
		anim.append(FadeIn(Tex("\\textbf{i}").scale(size).next_to(lines[0], LEFT).shift(UP * 1.5).set_fill(color = YELLOW)))
		for idx in idxs:
			anim.append(FadeIn(idx))
		self.play(*anim, run_time = 0.4)

		anim = []
		anim.append(FadeIn(Tex("\\textbf{A[i]}").scale(size).next_to(lines[0], LEFT)))
		for pair in pairs:
			anim.append(FadeIn(pair[0]))
			anim.append(FadeIn(pair[1]))
		self.play(*anim, run_time = 0.4)
	
		
		best = -1000
		bNum = Tex(str(best)).scale(2).shift(DOWN * 2 + RIGHT * 2)
		bS = SurroundingRectangle(bNum, buff = 0.2).set_stroke(color=GREEN)
		self.play(FadeIn(bNum), FadeIn(bS), FadeIn(Text("answer:").next_to(bS, UP).set_fill(color=GREEN)))

		gr = Tex(">").scale(1.7).next_to(bS, LEFT).set_fill(color=GREEN)
		le = Tex("<").scale(1.7).next_to(bS, LEFT).set_fill(color=RED)


		for i, pair in enumerate(pairs):
			x = minX + step * (i)
			val = arr[i][0] + arr[i][1]
			ffirst = Tex().become(pair[0])
			ssecond = Tex().become(pair[1])
			num = Tex(val).scale(size).move_to([x + step/2, 0, 0])
			self.play(ffirst.animate.become(num), ssecond.animate.become(num))

			self.remove(ffirst)
			num = ssecond
			
			if (val % 2 == 1):
				self.play(num.animate.set_fill(color=RED), FadeOut(num))
			else:
				self.wait(0.4)
				self.play(num.animate.next_to(gr, LEFT).scale(2/size))
				if (val > best):
					self.play(FadeIn(gr), run_time=0.4)
					self.wait(0.4)
					self.play(num.animate.move_to(bNum), FadeOut(bNum), run_time=0.4)
					bNum = num
					best = val 
					self.play(FadeOut(gr), run_time=0.4)
				else:
					self.play(FadeIn(le), run_time=0.4)
					self.wait(0.4)
					self.play(FadeOut(le), FadeOut(num), run_time=0.4)
		self.wait(1)
	
