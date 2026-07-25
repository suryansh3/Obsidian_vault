---
title: What is Vision Used For? | Introduction
source: https://www.youtube.com/watch?v=qt1UfF0fn4w&list=PL2zRqk16wsdoz4eycyq7EmeV2KpE6JN76&index=3
author:
  - "[[First Principles of Computer Vision]]"
published: 2021-03-01
created: 2026-07-19
description: First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Com
tags:
  - clippings
  - "#IPA"
---
![](https://www.youtube.com/watch?v=qt1UfF0fn4w)

First Principles of Computer Vision is a lecture series presented by Shree Nayar who is faculty in the Computer Science Department, School of Engineering and Applied Sciences, Columbia University. Computer Vision is the enterprise of building machines that “see.” This series focuses on the physical and mathematical underpinnings of vision and has been designed for students, practitioners, and enthusiasts who have no prior knowledge of computer vision.

## Transcript

### Intro

**0:03** · Now let's take a look at some of the things that vision is being used for today.

**0:07** · Each of these is a thriving industry unto itself.

**0:11** · I should mention that these are just examples and do not represent a complete list of vision applications.

**0:17** · Let's start with factory automation.

### Factory Automation: Vision-Gulded Robotics

**0:20** · As you probably know, manufacturing is highly automated these days.

**0:24** · For example, if you look at cars, they're almost entirely built by a large number of robots.

**0:30** · Now, these robots need computer vision to be able to deal with uncertainties that are inherent in any physical world.

**0:37** · For instance, if part A is being mounted on part B-- if there's any uncertainty with respect to the position of either one of these, vision is the only thing that can come to your rescue-- so vision guided robotics is a very large application domain.

**0:52** · And then talking about factory automation, you have visual inspection.

**0:56** · You know that the products are being manufactured at a very rapid pace.

**1:01** · In fact, the speed is so high that humans are simply not cut out to be able to inspect these parts.

**1:07** · At the same time, the size of the components going into these products is diminishing rapidly-- much smaller than the human eye can even see-- so computer vision today plays a very big role, it's absolutely vital to visual inspection in factory automation.

**1:24** · And then there is OCR, or Optical Character Recognition-- so in this particular example that you're seeing, you have a traffic system-- the traffic system knows that your car is moving too fast.

**1:36** · It's able to automatically read your license plate using OCR and then send a ticket to your home.

**1:44** · OCR has other applications such as the digitization of physical books, or authentication of signatures on a check, or even scanning envelopes and packages for mailing addresses and postal services.

**2:00** · It's a very widely used technology in computer vision.

**2:06** · And then you have biometrics.

**2:08** · Biometrics is using your physical characteristics to determine your identity.

**2:14** · So in this particular case, you see that the iris of your eye-- right here, the iris-- has a pattern inside of it.

**2:22** · It turns out that this pattern is almost as unique as your DNA, and can be used almost uniquely identify you for access control and other applications.

**2:34** · And then talking about biometrics, you have, of course, the very popular application of face detection and recognition.

### Biometrics: Face Detection and Recognition

**2:42** · Today, face detection is so mature that pretty much any image, you're able to find faces very robustly.

**2:51** · And this has applications for organizing your photos in your personal collection, or in security applications where you want to find suspicious people.

**3:01** · And in fact, you can go in and analyze the detected face regions to recognize the identity of the person as well.

**3:09** · Now here's an interesting application that I came across at Shinagawa Station in Japan-- it's a vending machine, we'll call it intelligent marketing.

### Intelligent Marketing: Vending Machine with Face Detection

**3:18** · You walk up to it and it's able to detect your gender and your rough age, and then show you-- display on the screen-- various products that may be of interest to you.

**3:31** · Another interesting domain for computer vision is tracking.

### Security: Object Detection and Tracking

**3:35** · You want to be able to track objects as they move through complex spaces.

**3:40** · Imagine people walking through crowds-- you want to be able to track them even when they're obstructed by other objects or other people and then continue to follow them.

**3:50** · In fact, today's tracking systems can track people using a camera, and as the person leaves the field of view of one camera, that camera then passes on-- or hands over-- the person to another camera in the system.

**4:09** · Now here is an application of computer vision that I'm sure you've used, but you may not be aware of it-- which is the optical mouse.

**4:17** · It turns out that inside the optical mouse is a complete computer vision system.

**4:22** · It has a tiny camera which captures images at very low resolution, but very high frame rate.

### Human Computer Interaction: Optical Mouse

**4:29** · It has a little lighting system that's able to illuminate the surface that the mouse is sitting on.

**4:34** · And using the pattern that this camera detects, it's able to then determine the motion of the mouse with respect to the surface that it sits on.

**4:43** · And this information is passed on, say, for instance, to your computer to control the cursor on your screen or your monitor.

### Entertainment and Gaming: Kinect

**4:52** · And then, of course, you have gaming.

**4:55** · If you look at pretty much any gaming console today-- be it Kinect or Playstation-- it's packed with vision sensors which are able to capture human beings in full body motion.

**5:06** · And this has, of course, unleashed an entirely new breed of interesting, engaging games.

**5:14** · Computer vision is also used for special effects in both movies as well as animations.

### Visual Effects Motion and Performance Capture

**5:21** · Here on the left, you see Doug Roble.

**5:23** · Doug has a headgear, which has a camera mounted on it, which is looking back at him-- and this camera produces an image that looks like this.

**5:31** · This imaging system is able to-- in real time-- extract Doug's expression in 3D.

**5:37** · And then this expression is mapped to a virtual character, such as Elbor, in this particular case.

**5:44** · Here's another instance of Doug-- another expression-- and that is being successfully mapped to Elbor.

**5:50** · In fact Doug Roble has given an entire Ted Talk through one of his virtual characters-- you should check it out.

**5:58** · Here's another application of vision which is for augmented reality-- AR.

### Augmented Reality: Face Manipulation

**6:03** · You're looking at Jian Wang here and his picture has been taken using the Snapchat camera.

**6:09** · And under the hood, in the Snapchat camera, it's able to extract Jian's face model in 3D.

**6:16** · There's a complete mesh that you see here, which is this 3D face model.

**6:20** · Using this face model, which is extracted in real time-- frame for frame-- you're able to manipulate Jian's face.

**6:27** · For instance, you might be able to imagine what he may have looked like when he was a young boy, or what he will look like when he is an old man.

**6:39** · Another very wide application domain for vision is visual search.

### Visual Search: Landmark Recognition

**6:43** · Visual search is a very general term-- it could be on the internet, but it could also be through your personal devices.

**6:50** · So here you see a person take a picture of a monument and you can immediately get historical information about the monument.

**6:58** · And then there is exploration-- vision for exploration-- I'm showing here the Mars Rover.

### Autonomous Navigation Space Exploration

**7:06** · The Mars Rover has various vision sensors-- you can actually see two cameras in the top here, but there are other vision sensors as well.

**7:14** · And since this is an area where people have actually not set foot on as yet, you need computer vision to be able to extract information and send it back to a remote location.

**7:25** · In this case, the terrain map of the surface of Mars-- and perhaps its material properties-- and this information is sent back to Earth.

**7:35** · And the same technology is important in the case of disaster zones, such as nuclear reactors and so on where you don't want to be sending human beings in there, and you try to send a robot with a computer vision system.

**7:51** · And then, of course, there is a very popular application domain of driverless cars.

### Autonomous Navigation: Driverless Car

**7:57** · These cars are packed with vision sensors-- visible light cameras, depth cameras, infrared cameras, and so on-- and all of these cameras together seek to extract detailed and very precise information about the geometry of the scene around the car in real time.

**8:19** · And this information is used by the car to make various decisions and different traffic scenarios-- needless to say, driverless cars are going to become a very big part of our everyday lives.

**8:33** · Here's another application domain, which is remote sensing.

### Remote Sensing

**8:37** · So think about a satellite that's orbiting the Earth-- it has high quality image sensors, cameras, and vision systems mounted on it and, therefore, is able to-- as it orbits-- collect information that can be used to reconstruct a three-dimensional map, say, for instance, of the surface of the Earth.

**8:57** · This information can be used in maps such as Google Maps, or it could be used to monitor a disaster zone, or explore the long term effects of climate change.

**9:09** · And, finally, I want to mention medical imaging, which is a huge application domain for computer vision.

### Medical Image Analysis

**9:15** · Now, in vision, we typically capture images using consumer cameras-- which are brightness and color images and the visible light spectrum-- the modalities are different in medical imaging.

**9:26** · You could have X-ray images, or ultrasound images, or magnetic resonance images-- but irrespective, the models and methods developed in computer vision often directly are useful applicable to medical imaging applications.

**9:43** · So in this case, for instance, you could use these techniques to recover anatomical structures, and perhaps even give some initial diagnosis to aid the physician.

**9:56** · So I hope I've convinced you that vision has enormous utility and that is why it is a topic of great interest today.