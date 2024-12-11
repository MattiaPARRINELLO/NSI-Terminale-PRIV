from manim import *
indexFontSizes = 35

class MergeSort(Scene):
    def construct(self):
        array = [1, 5, 3, 2]
        boxes = [Square(fill_opacity=0)   
             .scale(0.5)
             .shift(RIGHT*i)
              for i in range(len(array))]
        numbers = [Tex(str(array[i]))
                   .move_to(boxes[i])
                   for i in range(len(array))]

        group = VGroup(*boxes, *numbers)
        group.move_to(ORIGIN)
        numbersGroup = VGroup(*numbers)
        boxesGroup = VGroup(*boxes)
        txt = Text("Merge Sort", font_size=50)
        self.add(txt)
        self.wait(1)
        self.play(txt.animate.shift(UP*3.5).scale(0.5))
        self.play(Write(boxesGroup), Write(numbersGroup))
        self.wait(1)
        self.play(ApplyMethod(group.shift, UP*2))
        # devide the array into two parts
        leftBoxes = VGroup(*boxes[:len(boxes)//2])
        leftNumbers = VGroup(*numbers[:len(boxes)//2])
        rightBoxes = VGroup(*boxes[len(boxes)//2:])
        rightNumbers = VGroup(*numbers[len(boxes)//2:])
        self.play(AnimationGroup(Circumscribe(leftBoxes, color=PURE_GREEN, buff=0), Circumscribe(rightBoxes, color=PURE_RED, buff=0)))
        # copy rightBoxes and shift down and left
        rightBoxesCopy = VGroup(*rightBoxes.copy())
        rightNumberCopy = VGroup(*rightNumbers)
        leftBoxesCopy = VGroup(*leftBoxes.copy())
        leftNumberCopy = VGroup(*leftNumbers)
        self.play(rightBoxesCopy.animate.shift(DOWN*2+RIGHT*2), leftBoxesCopy.animate.shift(DOWN*2+LEFT*2), rightNumberCopy.animate.shift(DOWN*2+RIGHT*2), leftNumberCopy.animate.shift(DOWN*2+LEFT*2))
        self.wait(1)
        #divide the right part into two parts
        leftLeftBoxes = VGroup(*leftBoxesCopy[:len(leftBoxes)//2])
        leftRightBoxes = VGroup(*leftBoxesCopy[len(leftBoxes)//2:])
        rightLeftBoxes = VGroup(*rightBoxesCopy[:len(rightBoxes)//2])
        rightRightBoxes = VGroup(*rightBoxesCopy[len(rightBoxes)//2:])
        self.play(Circumscribe(leftLeftBoxes, color=PURE_GREEN, buff=0), Circumscribe(leftRightBoxes, color=PURE_RED, buff=0), Circumscribe(rightLeftBoxes, color=PURE_GREEN, buff=0), Circumscribe(rightRightBoxes, color=PURE_RED, buff=0))
        leftLeftBoxesCopy = VGroup(*leftLeftBoxes.copy())
        leftRightBoxesCopy = VGroup(*leftRightBoxes.copy())
        rightLeftBoxesCopy = VGroup(*rightLeftBoxes.copy())
        rightRightBoxesCopy = VGroup(*rightRightBoxes.copy())
        # move the numbers to the new positions
        leftLeftNumbers = VGroup(*leftNumberCopy[:len(leftNumberCopy)//2])
        leftRightNumbers = VGroup(*leftNumberCopy[len(leftNumberCopy)//2:])
        rightLeftNumbers = VGroup(*rightNumberCopy[:len(rightNumberCopy)//2])
        rightRightNumbers = VGroup(*rightNumberCopy[len(rightNumberCopy)//2:])

        self.play(leftLeftBoxesCopy.animate.shift(DOWN*2+LEFT*1), leftRightBoxesCopy.animate.shift(DOWN*2+RIGHT*1), rightLeftBoxesCopy.animate.shift(DOWN*2+LEFT*1), rightRightBoxesCopy.animate.shift(DOWN*2+RIGHT*1), leftLeftNumbers.animate.shift(DOWN*2+LEFT*1), leftRightNumbers.animate.shift(DOWN*2+RIGHT*1), rightLeftNumbers.animate.shift(DOWN*2+LEFT*1), rightRightNumbers.animate.shift(DOWN*2+RIGHT*1))
        self.wait(1)
        # display a < between leftLeftNumbers and leftRightNumbers
        temp = VGroup(*leftLeftBoxesCopy, *leftRightBoxesCopy)
        superiorto = Tex("$<$").move_to(temp.get_center())
        self.play(Write(superiorto), temp.animate.set(color = GREEN))
        self.play(FadeOut(superiorto), temp.animate.set(color = WHITE), leftLeftNumbers.animate.shift(UP*2+RIGHT*1), leftRightNumbers.animate.shift(UP*2+LEFT*1), FadeOut(leftLeftBoxesCopy), FadeOut(leftRightBoxesCopy))
        temp = VGroup(*rightLeftBoxesCopy, *rightRightBoxesCopy)
        inferiorTo = Tex("$>$").move_to(temp.get_center())
        self.play(Write(inferiorTo), temp.animate.set(color = RED))
        self.play(Swap(rightLeftNumbers[0], rightRightNumbers[0]), Transform(inferiorTo, Tex("$<$").move_to(temp.get_center())), temp.animate.set(color = GREEN))
        self.wait(1)
        self.play(FadeOut(inferiorTo), temp.animate.set(color = WHITE), rightLeftNumbers.animate.shift(UP*2+LEFT*1), rightRightNumbers.animate.shift(UP*2+RIGHT*1), FadeOut(rightLeftBoxesCopy), FadeOut(rightRightBoxesCopy))
        rightLeftNumbers[0], rightRightNumbers[0] = rightRightNumbers[0], rightLeftNumbers[0]
        aText = Tex("$A$").move_to(leftBoxesCopy.get_center()+UP*1)
        bText = Tex("$B$").move_to(rightBoxesCopy.get_center()+UP*1)
        self.play(Write(aText), Write(bText))
        self.wait(1)
        leftLeftBoxesCopyCopy = VGroup(*leftLeftBoxes.copy())
        leftRightBoxesCopyCopy = VGroup(*leftRightBoxes.copy())
        rightLeftBoxesCopyCopy = VGroup(*rightLeftBoxes.copy())
        rightRightBoxesCopyCopy = VGroup(*rightRightBoxes.copy())
        firstElA = VGroup(*leftLeftNumbers[0], *leftLeftBoxesCopyCopy[0])
        firstElB = VGroup(*rightLeftNumbers[0], *rightLeftBoxesCopyCopy[0])
        self.play(firstElA.animate.shift(DOWN*2+RIGHT*2), firstElB.animate.shift(DOWN*2+LEFT*1))
        temp = VGroup(*firstElA, *firstElB)
        superior = Tex("$<$").move_to(temp.get_center())
        self.play(Write(superior), leftLeftBoxesCopyCopy.animate.set(color = GREEN), rightLeftBoxesCopyCopy.animate.set(color = GREEN))
        self.play(FadeOut(superior), leftLeftBoxesCopyCopy.animate.set(color = WHITE), rightLeftBoxesCopyCopy.animate.set(color=WHITE), leftLeftNumbers[0].animate.shift(UP*4).set(color=WHITE), rightLeftNumbers[0].animate.shift(UP*4+LEFT*2).set(color = WHITE), FadeOut(leftLeftBoxesCopyCopy[0]), FadeOut(rightLeftBoxesCopyCopy[0]))
        self.wait(1)
        lastElA = VGroup(*leftRightNumbers[-1], *leftRightBoxesCopyCopy[-1])
        lastElB = VGroup(*rightRightNumbers[-1], *rightRightBoxesCopyCopy[-1])
        self.play(lastElA.animate.shift(DOWN*2+RIGHT*1), lastElB.animate.shift(DOWN*2+LEFT*2))
        temp = VGroup(*lastElA, *lastElB)
        inferior = Tex("$>$").move_to(temp.get_center())
        self.play(Write(inferior), leftRightBoxesCopyCopy.animate.set(color = RED), rightRightBoxesCopyCopy.animate.set(color = RED))
        self.play(Swap(leftRightNumbers[-1], rightRightNumbers[-1]), Transform(inferior, Tex("$<$").move_to(temp.get_center())), leftRightBoxesCopyCopy.animate.set(color = GREEN), rightRightBoxesCopyCopy.animate.set(color = GREEN))
        self.wait(1)
        self.play(FadeOut(inferior), leftRightBoxesCopyCopy.animate.set(color = WHITE), rightRightBoxesCopyCopy.animate.set(color=WHITE), leftRightNumbers[-1].animate.shift(UP*4).set(color=WHITE), rightRightNumbers[-1].animate.shift(UP*4+RIGHT*2).set(color = WHITE), FadeOut(leftRightBoxes[-1]), FadeOut(rightRightBoxes[-1]), FadeOut(leftRightBoxesCopyCopy[-1]), FadeOut(rightRightBoxesCopyCopy[-1]), FadeOut(aText), FadeOut(bText), FadeOut(leftLeftBoxes), FadeOut(rightLeftBoxes[-1]))
        numbersGroup = VGroup(leftRightNumbers[-1], rightRightNumbers[-1], leftLeftNumbers[0], rightLeftNumbers[0])
        totalGroup = VGroup(numbersGroup, boxesGroup) 
        self.play(totalGroup.animate.shift(DOWN*2).scale(1.4))
        for i in boxesGroup:
            self.play(Circumscribe(i, color=PURE_GREEN, buff=0, time_width=2), run_time=0.5)
            self.play(i.animate.set(color=PURE_GREEN), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(totalGroup))
        self.play(txt.animate.shift(DOWN*3.5).scale(2))
        self.wait(1)





