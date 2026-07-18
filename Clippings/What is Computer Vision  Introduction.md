---
title: "What is Computer Vision? | Introduction"
source: "https://www.youtube.com/watch?v=wVE8SFMSBJ0&list=PL2zRqk16wsdoz4eycyq7EmeV2KpE6JN76&index=2"
author:
  - "[[First Principles of Computer Vision]]"
published: 2021-03-01
created: 2026-07-18
description: "First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Com"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=wVE8SFMSBJ0)

First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Computer Vision is the enterprise of building machines that “see.” This series focuses on the physical and mathematical underpinnings of vision and has been designed for students, practitioners, and enthusiasts who have no prior knowledge of computer vision.

## Transcript

### Intro

**0:03** · Vision is our most powerful sense.

**0:06** · It allows us to interact with the physical world without making any direct physical contact.

**0:12** · It turns out that roughly 60% of your brain is in one way or the other involved in the process of visual perception.

**0:19** · Just think about that for a second.

**0:21** · Vision is so powerful that we are able to navigate this very complex world that we live in seamlessly.

**0:28** · Computer vision is the enterprise of building machines that can see.

**0:34** · Now, you may be wondering, given that the human visual system is so powerful, why even bother to build machines that can emulate it?

**0:42** · Well, there are several reasons.

**0:45** · First, there are many chores we perform on a daily basis that we would rather have done by a machine so we can free up the time to devote to more rewarding activities.

**0:55** · Examples of such chores might be tidying your home or driving to work.

**1:00** · Second, while our vision system is truly powerful, it tends to be more qualitative than quantitative.

**1:07** · It is not particularly good at making precise measurements of things in the physical world.

**1:14** · And lastly, perhaps most importantly, a computer vision system can be designed to surpass the capability of human vision and extract information about the world that we humans simply cannot perceive.

### What is Computer Vision?

**1:30** · Here are the basic elements of a computer vision system.

**1:33** · On the right here, you see a three dimensional scene.

**1:36** · This scene is lit by some form of lighting.

**1:39** · It could be very simple outdoor lighting as in the case of a single point light source, the sun, or it could be more complex indoor lighting with various types of lamps.

**1:50** · Irrespective, without lighting, there is no vision.

**1:54** · And the light from these various light sources falls in the scene and is scattered or reflected by the scene in many different directions.

**2:02** · And a small fraction of this light is scattered in the direction of this camera shown here, which plays the role of the human eye.

**2:11** · The camera takes light from the three dimensional scene to produce a two dimensional image.

**2:17** · This image is passed on to your vision software.

**2:20** · And the goal of this vision software is to come up with a symbolic description of the scene.

**2:26** · For example, it might be able to say that there are two wine bottles, wine glasses.

**2:31** · There's bread, cheese on the table.

**2:34** · And a more sophisticated vision system may be able to tell you how fresh the bread is, exactly what types of cheese are on the table, and perhaps even the vintage of the wine.

**2:47** · So what would be a concise definition for computer vision?

### But, What Really is Computer Vision?

**2:50** · Well, it really depends on the background of the person that you ask.

**2:54** · For instance, David Maher, who wrote one of the first textbooks on vision, said that vision is automating human visual processes.

**3:03** · He was really looking at computer vision as the emulation of human vision.

**3:09** · Others have said that vision is an information processing task.

**3:14** · Berthold Horn, who wrote the book Robot Vision, said that vision is inverting image formation.

**3:21** · Let's think about this for a second.

**3:23** · An image is the projection of a three dimensional world onto a two dimensional plane.

**3:30** · And so now, one can think about computer vision as taking this two dimensional image and somehow walking back into the three dimensional world to say things about the objects that compose that world.

**3:43** · So another way to say this is perhaps vision is the inverse of graphics.

**3:48** · In computer graphics, as you know, you create very elaborate three dimensional models of objects.

**3:54** · You place them in a scene.

**3:56** · You illuminate the scene with some type of lighting.

**3:59** · And you seek to obtain a photorealistic image of the scene.

**4:03** · In our case here, in vision, we're going to start with an image that's given to us and try and walk back into the three dimensional world and say things about the objects that make up that world.

**4:15** · My PhD advisor, Takeo Kanade, used to say that irrespective of the definition, vision is fun.

**4:22** · And that's true.

**4:24** · But perhaps more importantly, vision is really useful.

**4:29** · Now, vision deals with images.

### Vision Deals with Images

**4:31** · An image is an array of pixels.

**4:34** · Pixel, by the way, is short for picture element.

**4:37** · And each pixel in your image records information about a corresponding point in the scene.

**4:43** · If you look at consumer cameras, a pixel provides the brightness and color of the corresponding point in the scene.

**4:51** · More recently, we have seen more sophisticated cameras that can measure at each pixel the depth or the distance of the point in the scene.

**4:59** · And in the years to come, we will see, I believe, cameras that can also detect the material properties of points in the scene.

**5:07** · We will be able to tell whether a point is made of glass or wood or plastic or metal.

**5:14** · So with the passage of time, cameras are going to get more sophisticated.

**5:18** · They're going to be able to extract information that goes well beyond what the human eye can.

**5:24** · And therefore, computer vision systems will be able to perceive things about the scene that you and I simply cannot see.

**5:32** · Now, needless to say, images are interesting.

### Images Are Interesting

**5:36** · You simply open your eyes and take a look at this image here.

**5:39** · And you'll see there are two boys.

**5:41** · One of them is taking a bath.

**5:44** · You get a sense for the three dimensional structure of the scene, the vegetation, perhaps the time of day, and maybe even the weather because you see a bit of fog in the background.

**5:54** · And in fact, you can even get a sense for the playful mood of the scene.

**5:58** · Maybe the sensation of what the boy may be feeling as the water strikes his head.

**6:03** · All of this in a fraction of a second by simply opening your eyes and taking a look at the image.

**6:09** · But for you to understand how challenging computer vision is, I want you to look at not this image, but its digital equivalent, which is this.

**6:19** · It's nothing but an array of numbers.

**6:22** · And it is from this set of numbers that we seek to extract all the information that you and I perceived in the previous slide.

**6:30** · This should give you a sense for why vision is really challenging, and why vision is fun.

**6:39** · So where do we stand?

**6:40** · Well, there's been about 50 years of research in computer vision.

### Vision Research

**6:44** · And we've learned a few things.

**6:46** · First, the obvious-- vision is hard.

**6:49** · Second, it's a highly multidisciplinary field.

**6:53** · It's not an isolated field.

**6:55** · It draws on optics for imaging, signal processing as in electrical engineering, algorithms in computer science, and even neuroscience and psychology and sometimes even biology.

**7:09** · But we can say today that a considerable amount of progress has been made.

**7:14** · And we've begun to see some very successful applications of vision.

**7:19** · But I should mention that we have just scratched the surface.

**7:23** · In the coming decades, we can expect computer vision to have a profound impact on the way that we live our lives.