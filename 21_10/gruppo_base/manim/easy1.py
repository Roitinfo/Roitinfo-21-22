from manim import *

class Easy1(Scene):
	def construct(self):
		arr = []
		with open("input/input1.txt") as file:
			lines = file.readlines()
			n = int(lines[0].split()[0])
			arr = lines[1].split()[:n]
			for i in range(n):
				arr[i] = int(arr[i])

		minX = -5
		step = 2 
		size = step * 0.8
		nums = []
		idxs = []
		lines = []
		for i, n in enumerate(arr):
			x = minX + step * (i)

			line = Line([x, 3.5, 0], [x, 1.5, 0]);
			num = Tex(str(n)).scale(size).move_to([x + step/2, 2, 0])
			idx = Tex(str(i)).scale(size).move_to([x + step/2, 3, 0]).set_fill(color = YELLOW)
			nums.append(num)
			idxs.append(idx)
			lines.append(line)

		self.play(Create(Line([-7, 2.5, 0], [7, 2.5, 0])), run_time = 0.4)

		anim = []
		for line in lines:
			anim.append(Create(line))

		self.play(*anim, run_time = 0.4)
		
		anim = []
		anim.append(FadeIn(Tex("\\textbf{i}").scale(size).next_to(lines[0], LEFT).shift(UP * 0.5).set_fill(color = YELLOW)))
		for idx in idxs:
			anim.append(FadeIn(idx))
		self.play(*anim, run_time = 0.4)

		anim = []
		anim.append(FadeIn(Tex("\\textbf{A[i]}").scale(size).next_to(lines[0], LEFT).shift(DOWN * 0.5)))
		for num in nums:
			anim.append(FadeIn(num))
		self.play(*anim, run_time = 0.4)
		
		best = -1000
		bNum = Tex(str(best)).scale(2).shift(DOWN + RIGHT * 2)
		bS = SurroundingRectangle(bNum, buff = 0.2).set_stroke(color=GREEN)
		self.play(FadeIn(bNum), FadeIn(bS), FadeIn(Text("answer:").next_to(bS, UP).set_fill(color=GREEN)))

		gr = Tex(">").scale(1.7).next_to(bS, LEFT).set_fill(color=GREEN)
		le = Tex("<").scale(1.7).next_to(bS, LEFT).set_fill(color=RED)

		s = SurroundingRectangle(nums[0], buff = 0.15).set_stroke(color=RED)
		self.play(Create(s))

		for i, num in enumerate(nums):
			if num != nums[0]:
				self.play(s.animate.move_to(num))

			nnum = Tex().become(num)
			self.play(nnum.animate.next_to(gr, LEFT).scale(2/size))
			n = arr[i]

			if (n > best):
				self.play(FadeIn(gr), run_time=0.4)
				self.wait(0.4)
				self.play(nnum.animate.move_to(bNum), FadeOut(bNum), run_time=0.4)
				bNum = nnum
				best = n
				self.play(FadeOut(gr), run_time=0.4)
			else:
				self.play(FadeIn(le), run_time=0.4)
				self.wait(0.4)
				self.play(FadeOut(le), FadeOut(nnum), run_time=0.4)

		self.play(Uncreate(s))
		self.wait(1)
