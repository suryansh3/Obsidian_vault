---
title: How Do Humans Do It? | Introduction
source: https://www.youtube.com/watch?v=EOUcIto5WMU&list=PL2zRqk16wsdoz4eycyq7EmeV2KpE6JN76&index=4
author:
  - "[[First Principles of Computer Vision]]"
published: 2021-03-01
created: 2026-07-19
description: First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Com
tags:
  - clippings
  - "#IPA"
---
![](https://www.youtube.com/watch?v=EOUcIto5WMU)

First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Computer Vision is the enterprise of building machines that “see.” This series focuses on the physical and mathematical underpinnings of vision and has been designed for students, practitioners, and enthusiasts who have no prior knowledge of computer vision.

## Transcript

### Intro

**0:03** · Before we begin to develop tools to help us solve vision problems, it's worth taking a look at how our human visual system works.

### Human Eye and Visual Cortex

**0:13** · So here, you see the human eye and the visual cortex.

**0:17** · Here you see the eye in the front.

**0:19** · The eye has a lens which projects the three-dimensional world onto a two-dimensional image.

**0:26** · This two-dimensional image is being formed on the retina, which is in the back here.

**0:32** · The retina, by the way, has some cells within it that do some early visual processing.

**0:38** · So there's a little bit of information reduction that's happening on the retina itself.

**0:43** · And then the reduced image, so to speak, travels through the optic nerve right here and goes to the lateral geniculate nucleus, which acts like a relay.

**0:54** · It's able to figure out what information needs to go to which part of the brain.

**0:58** · So it sends that information then back to the visual cortex right here.

**1:02** · And you can see the different parts of the visual cortex have been given different colors.

**1:08** · And that's to show you the parts that are responsible for analysis of shape, of color, of motion, of texture, and so on and so forth.

**1:19** · So there's a lot we know about the human visual system.

**1:23** · And yet, it's amazing to me how little we know.

**1:26** · We know, for instance, roughly where motion analysis takes place.

**1:31** · But we have no idea exactly what the circuit diagram, if you will, is of that particular part of the brain.

**1:40** · We don't know how the neurons are connected to each other and what their weights are.

**1:45** · So we don't have a detailed architecture or a circuit, if you will, that can be mapped to silicon, so we can emulate the human visual system.

**1:54** · So in short, vision is easy for us.

**1:58** · But we are very far from understanding how we actually do it.

**2:03** · So what do we do?

### What do we do?

**2:05** · Well, we reinvent.

**2:08** · This might sound unfortunate to you, but not quite.

**2:12** · As you can imagine, there are many applications of vision that require functionality and precision that go well beyond what the human visual system is capable of.

**2:23** · While human vision is remarkable in its versatility and is able to cope with many complex real world situations, it is more of a qualitative system than a quantitative one.

**2:35** · For instance, if you want to know how many millimeters this pencil is in terms of its length, the human visual system can only give you very rough estimates.

**2:46** · Such estimates are not useful in many domains, such as factory automation or medical imaging.

**2:53** · While no computer vision system has yet been developed that is as versatile as the human one, there are many computer vision systems in use today that demonstrate much higher precision and reliability than ours.

**3:08** · In short, for many tasks that require vision, the human visual system may indeed be the wrong system to emulate.

**3:17** · Furthermore, human vision is more fallible than we like to believe.

**3:22** · You see, when you and I perceive something incorrectly, we do not have a voice in our head telling us we are wrong.

**3:28** · We see that what we see, and we believe it to be accurate.

**3:33** · To demonstrate this, let's take a look at some well-known optical illusions.

**3:39** · So here's the first illusion I want to show you, which is Fraser's spiral.

### Illusions: Fraser's Spiral

**3:44** · When you and I take a look at this picture, you see a spiral emerging from the center.

**3:49** · We can agree on this.

**3:51** · It turns out there is no spiral here.

**3:54** · If you follow one of these contours, if you follow this one, say, for instance and go all the way around like so, you find that you come back to exactly the same place.

**4:06** · In other words, this is actually a set of concentric circles.

### Illusions: Checker Shadow

**4:12** · Here's another one.

**4:13** · It's called the Checker Shadow Illusion by Ted Adelson.

**4:17** · So here you see a checkerboard pattern as the floor.

**4:20** · And you see this cylinder sitting on top of it.

**4:24** · And I'd like you to pay attention to patch A and patch B. This is patch A right here and patch B.

**4:31** · You and I would agree that patch A is much darker than patch B.

**4:36** · But now what I'm going to do is to hide the rest of the scene and show you just patch A and patch B.

**4:42** · And you see that patch A and patch B have exactly the same brightness.

**4:47** · So what's going on here?

**4:49** · Well, it turns out that our visual system is able to figure out in this case, or in any case, that the illumination is varying over the scene.

**4:58** · It's gradually varying.

**5:00** · It's able to detect this spatially varying illumination and use it to compensate for the brightness values in the image itself, and therefore, able to figure out that patch A is made of darker material than patch B, although both of them actually have exactly the same brightness.

**5:17** · Here's another interesting one.

### Illusions: Donguri Wave

**5:18** · It's called the Donguri wave.

**5:21** · Take a look at this picture and move your eye around.

**5:23** · And as you do, you'll see that the red leaves actually wave around.

**5:29** · You can see motion.

**5:30** · But this is actually perceived motion without any motion.

**5:34** · This is obviously a static photograph and not a video.

**5:38** · And then there is forced perspective.

### Illusions: Forced Perspective

**5:41** · So in this room, you see two women.

**5:43** · The woman on the right seems much shorter and smaller than the one on the left.

**5:48** · It turns out they are of exactly the same height.

**5:52** · And the reason you see this very striking difference in their body size is because the room itself is not a cuboid, but in fact, it tapers.

**6:05** · The distance between the floor and the ceiling increases as you move away from the camera.

**6:10** · And this forces an illusion which makes objects in the scene appear different in terms of their relative sizes.

### Visual Ambiguities

**6:22** · And then there is a difference between illusions and ambiguity.

**6:26** · An ambiguity arises from the fact that in vision, you have a three-dimensional world that's being projected onto a two-dimensional image.

**6:34** · So you are, in some ways, dropping one dimension.

**6:37** · And this creates some fundamental ambiguities.

**6:40** · In this particular case, if you look at a vertex right here, and if you stare at this vertex, you see that at times, it looks like a cube that is popping out and sometimes jutting in, so concave or convex.

**6:55** · And depending on which interpretation your mind latches on to, you either see six cubes or seven cubes.

**7:02** · And in fact, if you keep staring at it, this interpretation can flip over time.

**7:06** · Both are equally likely because it's an ambiguity.

**7:11** · And there are higher levels of ambiguity.

**7:13** · In this case on the left here, you could see perhaps a young girl turned away substantially.

**7:20** · There's a nose of the girl, say, for instance.

**7:22** · And this could be her necklace.

**7:24** · Or it could be an old woman's full profile with a very large nose right here and perhaps the mouth here.

**7:32** · It's a matter of perspective, I guess.

**7:35** · And on the right, this could be two faces looking at each other, the silhouettes of two faces, or it could be a vase.

**7:44** · And here's my favorite visual ambiguity.

**7:47** · So in this case, when you and I look at this, on the left, we can agree that we see a large mound with a little crater in the center.

**7:58** · And if I asked you the question, what are you going to see if I flip this picture upside down, you'll probably say that you're going to expect to see a mound hanging upside down.

**8:10** · But in fact, if I actually flip this picture, you see a large crater with a little mound in the center.

**8:18** · Why does this happen?

**8:20** · Well, it turns out that we live in a world where illumination comes, generally speaking, from above-- for instance, the sun.

**8:28** · You seldom have light coming from beneath us.

**8:32** · So we use this assumption because it's actually not possible to uniquely interpret the shading of an object.

**8:39** · You use this assumption first, and then try and interpret the shading of an object.

**8:44** · In doing so, you're able to create these two different interpretations of the same object by first invoking the assumption that the lighting is from above us.

**8:56** · And then there is the difference between seeing and thinking.

### Seeing vs. Thinking

**9:00** · This is the Kanizsa Triangle.

**9:03** · In this case, in the center, you see a white triangle.

**9:08** · In fact, this white triangle in the center seems to be brighter than the white background.

**9:13** · And it seems to be jutting out a bit, that it's closer in depth than the rest of the scene.

**9:18** · But there is no triangle here.

**9:20** · There are actually three Pac-Man-like fragmented discs very carefully configured and aligned that give you the illusion of a white triangle.

**9:30** · Your brain is actually filling in this information.

**9:34** · It believes that there is a triangle.

**9:36** · This is the difference between seeing and thinking.