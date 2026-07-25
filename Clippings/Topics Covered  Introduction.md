---
title: Topics Covered | Introduction
source: https://www.youtube.com/watch?v=jJd0jpku8qs&list=PL2zRqk16wsdoz4eycyq7EmeV2KpE6JN76&index=5
author:
  - "[[First Principles of Computer Vision]]"
published: 2021-03-01
created: 2026-07-19
description: First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Com
tags:
  - clippings
  - IPA
---
![](https://www.youtube.com/watch?v=jJd0jpku8qs)

First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Computer Vision is the enterprise of building machines that “see.” This series focuses on the physical and mathematical underpinnings of vision and has been designed for students, practitioners, and enthusiasts who have no prior knowledge of computer vision.

## Transcript

### Topics Covered

**0:03** · Now let's take a look at the topics covered in these lectures.

**0:07** · We're going to start with image formation and optics.

### Image Formation and Optics Where do Images Come From?

**0:11** · We're going to look at the mapping of a three-dimensional world to a two-dimensional plane using a lens.

**0:18** · So where do images come from?

**0:19** · And what is the relationship between the position of a point in 3D and its projection in its 2D image?

**0:27** · And for that matter, how does the brightness of a point in 3D relate to its brightness in the image as a creation of an optical image.

**0:37** · So once we have an optical image, we think about how to map this image, to record it, and create a digital image.

### Convert Optical Images to Electrical Signals

**0:45** · And this is done using image sensors.

**0:48** · By the way, image sensor technology has made tremendous advances in the last two decades.

**0:54** · In fact, that is one of the main reasons, we are witnessing this digital imaging revolution that we're living in this point in time.

**1:03** · So we look at different types of image sensors and how they actually convert optical images to digital images.

**1:11** · Then we look at the simplest type of image that you can deal with.

**1:15** · It's called a binary image.

**1:16** · These are two valued images.

**1:18** · For instance, the image on the left shown here, you can simply threshold it to create the image on the right.

**1:25** · This is often possible in very structured environments, like factory automation or manufacturing lines, where you can control both the illumination and the background.

**1:35** · Simple thresholding can give you a nice, clean silhouette or binary image of the object.

**1:41** · So once you have this binary image, very easy to store, easy to process.

**1:45** · You can robustly compute properties of the object, and therefore, create some very effective vision systems.

**1:53** · Next, we look at image processing.

**1:56** · Coming back to general gray-scale or color images, how do we transform an image into a new image that is more amenable to higher levels of visual processing.

**2:08** · So we're going to devote two lectures to image processing.

**2:11** · Here's an example.

**2:12** · You have an image on the left that you see here.

**2:15** · And you can see it's very grainy.

**2:17** · It has a lot of noise.

**2:19** · And by applying image processing tools, you can get the image on the right where pretty much all the noise is gone.

**2:27** · And at the same time, the visual features, the edges, and the colors are all preserved.

**2:33** · So we'll come up with an entire suite of image processing tools that we can have at our disposal as we go into higher levels of visual processing.

**2:44** · So then we're going to look at feature detection.

### Edge and Corner Detection Detecting Intensity Changes in the Image

**2:48** · And the first features we're going to look at are edge detectors and corner detectors.

**2:53** · We'll develop a framework for edge detection, a theory of edge detection.

**2:59** · And based on this theory, we'll develop a few different types of edge and corner detectors.

**3:05** · Now, when you apply an edge detector to an image such as the one on the left here-- in the center you have, what we call, an edge map, the strength of the edge at each point.

### Finding Continuous Lines from Edge Segments

**3:16** · Well, when you and I take a look at this, we can immediately figure out which edges belong to the same boundaries or contours.

**3:23** · But that's because the brain is doing it for us.

**3:26** · But, actually, this is just a set of edges.

**3:28** · And we need to go from these edges to boundaries such as the one shown here.

**3:33** · So we will develop algorithms for boundary detection.

**3:39** · And then, we're going to spend some time looking at a specific detector which is very powerful.

### 2D Recognition using Features Matching using "Interesting Points"

**3:44** · It's called the SIFT detector.

**3:46** · Scale-invariant feature transform.

**3:50** · So you see on the left here, all the dots that you see, the colored dots, these are SIFT features that have been detected by the algorithm.

**3:58** · They don't seem to be attached to edges per se but actually to blobs or interesting areas in the image.

**4:05** · And you can very robustly find these, even when the object is translated or rotated or scaled.

**4:13** · And that makes it really useful for recognition problems.

**4:16** · So, for instance, in the image on the right, you see the same object not only transformed, geometrically, but also obstructed partially.

**4:24** · And yet, you're able to match these features and find the object very effectively, very robustly.

**4:31** · So we look at SIFT features.

### Image Alignment and Stitching Combine multiple photos to create a larger photo

**4:35** · And then we look at a couple of applications, popular applications of feature detection.

**4:41** · So here is one which is the creation of a panorama from a set of images taken from roughly the same viewpoint but by rotating the camera.

**4:51** · So these are overlapping images.

**4:54** · We apply feature detection to these images.

**4:57** · These are the features that you see here.

**4:59** · And then from these three images, we are able to create a seamless panorama, wide-angle panorama, of the scene.

**5:07** · This is an algorithm that sits on most smartphones these days.

**5:11** · And we will see exactly how it works.

**5:16** · Next, we'll talk about the popular problem of face detection.

**5:19** · Faces, needless to say, are very important.

**5:23** · We'll develop a detector that can actually find faces and images under varying illumination conditions and pose conditions.

**5:33** · Everything we've discussed thus far focuses on extracting information on the image plane that is in 2D.

**5:40** · Next, we're going to lay the groundwork for developing algorithms that recover a three-dimensional structure of a scene from one or more images.

**5:49** · So we're going to now go from 2D to 3D.

**5:53** · So in this context, we're going to start with the radiometry and reflectance.

**5:58** · Radiometry is about measuring light, to be able to define how bright a surface is, how intense a light source is.

**6:06** · Once we have radiometric definitions in place, we look at what's called reflectance.

**6:12** · Why does silk look the way it does?

**6:15** · And why does it look different from velvet?

**6:17** · What are the reflectance models that drive these different manifestations of scattering of light?

**6:24** · So will define a few different reflectance models that will come in really handy.

**6:29** · Next, we'll take a look at photometric stereo which is the first method we're going to describe for recovering 3D shape information from images of an object taken under different lighting conditions.

**6:41** · So you have a three-dimensional object, you're looking at it from the same direction but you light it from different known directions.

**6:48** · And just the change in brightness at each point, in the stack of images, allows you to compute the surface normal that each point on the surface.

**6:58** · And then you can, if it's a continuous surface, integrate the surface normals to get the three-dimensional shape which is shown in the bottom here.

**7:08** · And then after that, we're going to look at the more challenging problem of shape from shading.

### Shape from Shading 3D Shape from a Single Image

**7:13** · The shape from shading, you're trying to recover a three-dimensional shape information from a single shaded image of the object.

**7:20** · Very challenging problem.

**7:22** · And in fact, it doesn't have a solution without throwing in additional constraints or assumptions.

**7:28** · So we look at what assumptions are reasonable to make.

**7:32** · And then develop an algorithm that takes you from the image on the left to the three-dimensional shape on the right.

**7:40** · Now, you may have noticed that when you look through a lens in say, for instance, a large digital SLR camera.

**7:47** · And you change the focus setting of the lens.

**7:51** · You see that points in the scene come into focus and go out of focus.

**7:55** · And when exactly a point comes into focus has something to do with the distance of the point from the camera.

**8:02** · And so we develop algorithms that can take a small number of images with different focus settings and recover the three-dimensional structure of the scene.

**8:12** · So here you see, a near-focused image and a far-focused image.

**8:17** · And from these two images, we are able to compute this detailed depth map, distance map, where the closer the point is, the brighter it is.

### Using Patterned Lighting to Recover Shape

**8:28** · And then, we're going to talk about active illumination.

**8:31** · I would say that in order to make vision really robust, whenever possible, one should use active illumination.

**8:39** · Say, for instance, in a assembly line or some kind of a conveyor belt situation.

**8:46** · You can actually control the lighting in these scenarios.

**8:49** · And when you can, you should.

**8:52** · Because when the illumination of a scene can be controlled, you can recover three-dimensional information on material properties of the scene with much greater robustness and accuracy than you can without controlling the illumination.

**9:07** · So here you see Michelangelo's David, the statue.

**9:11** · And it's being scanned using active illumination technique.

**9:15** · And you get this 3D model that you see on the right.

**9:19** · And it's a very precise model.

**9:21** · In fact, if you take a close look at it, you see, for instance, David's eye.

**9:25** · All the different surface undulations of captured with great fidelity.

### Camera Calibration Estimating Camera Parameters

**9:33** · And now we're going to talk about camera calibration.

**9:37** · In order to go from an image, where things are measured in pixels, back into the three-dimensional scene where things may be measured in millimeters.

**9:47** · You really need to know the mapping.

**9:49** · And this mapping is determined by a small number of camera parameters, its focal length here for instance, but many other parameters.

**9:58** · It turns out that a single image of an object of known structure, such as this cube shown here, is enough for you to determine all the camera's parameters.

**10:11** · So with the camera calibrated, we can now come up with techniques for recovering three-dimensional structure from two or more images of a scene.

**10:20** · The first approach we're going to look at is binocular stereo.

### Computing Depth using Two Views

**10:24** · So do this little experiment with me.

**10:27** · You have two hands.

**10:29** · You stick your index fingers out.

**10:32** · Hold one hand in front of you.

**10:34** · And then shut one of your eyes.

**10:36** · Now, take your other hand.

**10:38** · And you're going to bring it from behind you really fast.

**10:41** · And try and see if you can make the two index fingers meet.

**10:45** · And you find that it's pretty hard with one eye closed but much easier if you have two eyes open.

**10:51** · So the reason is that we use two eyes to actually perceive the depth of the three-dimensional scene.

**10:58** · The two eyes capture two slightly different images.

**11:02** · And those differences in these images is what we use to perceive depth.

**11:07** · And so we look at how we can develop algorithms that can recover depth from two or more images taken from different viewpoints.

**11:16** · Here you see your binocular stereo system with two cameras.

**11:19** · There's a right view here and a left view.

**11:22** · And from just these two views, we can compute this depth map shown here where the brighter the point is, the closer it is to the camera.

**11:33** · Now thus far, we have assumed that the scene is essentially static, not moving.

### Determining the Movement of Scene Points

**11:37** · But we know that everything is moving, essentially, all the time.

**11:42** · And so motion is really important and something that we'd like to measure.

**11:48** · So what you're seeing here on the top is three images taken while the camera moves just slightly.

**11:56** · So actually, the tree and the house and everything else is slightly displaced from frame to frame but displaced differently depending on how far they are.

**12:06** · So if you have a point moving in three-dimensional space, it's projection onto the image is called its motion field.

**12:13** · And when you can see this motion in the image, when it's measurable, it's called optical flow.

**12:20** · We'll develop an algorithm for optical flow.

**12:23** · And here you see optical flow vectors for this particular scene where the length of the vector tells you how fast it's moving.

**12:30** · And the direction is telling you which direction it's moving in.

**12:34** · And next, we're going to talk about structure from motion.

**12:37** · Here's an interesting fact.

**12:38** · If you take a camera and you move it around an object, like this one right here-- you see the camera being moved around this little sculpture, but it's being moved in an uncontrolled fashion.

**12:50** · It's just a hand-held video so to speak.

**12:54** · So you don't know the relative position of the camera from one frame to the next.

**12:59** · But it turns out that even with this casual video, you can recover the three-dimensional structure of the scene.

**13:06** · And what's interesting is, in addition to that, you can also determine how the camera moved in three-dimensional space.

**13:14** · This problem is called structure from motion.

**13:16** · And we'll develop algorithms for structure from motion.

**13:21** · Now with that, we will conclude 3D reconstruction and move on to the problem of perception.

**13:28** · The first problem in perception we want to look at is image segmentation, a really hard problem.

### Group pixels with similar visual characteristics.

**13:34** · The segmentation problem is grouping pixels together that have similar visual characteristics.

**13:40** · So for instance, in this image that you see right here, you want to come up with segments where each segment corresponds to its own a specific individual vegetable, or pepper in this particular case.

**13:54** · And you see that the algorithm comes up with this segmentation right here.

**13:58** · It's a hard problem because exactly what pixels belong to the same object has a lot to do with context.

**14:06** · For example, if I'm wearing a hat, is the object me with the hat on?

**14:13** · Or is the hat a separate object from me?

**14:16** · Depends on the context to a certain extent.

**14:18** · So image segmentation is an ill-defined problem and we'll see how we can come up with simple metrics for the similarity between pixels in an image and use that to come up with reasonable solutions for the segmentation problem.

**14:34** · Another perception problem we want to talk about is tracking.

### Object Tracking Determining the Movement of Objects in Videos

**14:38** · We want to be able to follow moving things through space and time.

**14:43** · And of course, if it's a very clean video of somebody walking down a street that would be an easy problem.

**14:49** · But when you look at, say, for instance, a person walking through the crowd in say Grand Central Station, that's a really challenging problem.

**15:00** · Because this person can go hidden from you at times, can be obstructed by other people, go behind a wall or a pillar.

**15:07** · And so we want to be able to develop algorithms that can robustly follow this person over space and time.

**15:14** · And that's the object tracking problem.

**15:18** · And then, finally, we are going to devote two lectures to the problem of recognition.

### Appearance Matching Object Recognition using Principle Component Analysis

**15:23** · The first one is based on appearance matching.

**15:26** · If I show you this object right here and I say, "Memorize it", what you would possibly do is pick up the object and look at it from different directions.

**15:36** · And these images that you're looking at, you would somehow use that to create a representation in your mind.

**15:42** · And then when I show you this object again, you wouldn't know that it is actually the object you saw before.

**15:48** · Well, we use a similar technique here which we call appearance matching.

**15:53** · Here you see a little toy truck.

**15:55** · It is shown to the camera under different orientations and under different lighting conditions so a large number of images are captured.

**16:05** · But then, that is too big a representation to hold in memory, so we use the mathematical technique called Principle Component Analysis to reduce the dimensionality of this data and come up with a very compact appearance manifold which is shown here on the right.

**16:23** · Now, if this object appears in a scene and you are able to segment it out, you can then use this appearance manifold to figure out whether it is indeed that object and what its supposed illumination might be.

**16:40** · And then, finally, we're going to conclude with artificial neural networks.

### Artificial Neural Networks Using Network of Neurons to Solve Complex Problems

**16:44** · These are very popular these days.

**16:48** · And we are going to show how you can construct a neural network to perform a complex mapping from an input image to an output result that we are looking for.

**16:59** · We'll start with describing what a neuron is.

**17:03** · And then go into how we can construct a neural network.

**17:07** · And finally, talk about the mathematics behind the back propagation algorithm which is used to train these networks from data that's given.