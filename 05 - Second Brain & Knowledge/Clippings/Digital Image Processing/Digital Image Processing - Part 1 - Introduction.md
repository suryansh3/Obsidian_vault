---
title: "Digital Image Processing - Part 1 - Introduction"
source: "https://www.youtube.com/watch?v=rSGMXktIsYI&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=1"
author:
  - "[[ASIP-Lab]]"
published: 2020-06-01
created: 2026-08-12
description: "Topics:1:57 What is Digital Image Processing (DIP)?6:00 The Origins of DIP10:10 DIP Applications20:24 Fundamental Steps in DIP25:20 Components of a DIP System26:19 Elements of Visual Perception"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=rSGMXktIsYI)

Topics:  
1:57 What is Digital Image Processing (DIP)?  
6:00 The Origins of DIP  
10:10 DIP Applications  
20:24 Fundamental Steps in DIP  
25:20 Components of a DIP System  
26:19 Elements of Visual Perception  
33:35 Light and the Electromagnetic Spectrum  
37:24 Image Sensing and Acquisition  
44:02 Image Sampling and Quantization

## Transcript

**0:02** · this is the first lecture of the course digital image processing which is offered there special topics course for both undergrad and graduate student in engineering and computer science so one thing that I should note is that the material that I present here or Drive

**0:28** · from the digital image processing book the fourth edition written by khandala and wood and you can purchase the book either from Amazon or from the publishers website so in the first

**0:47** · lecture these are the topics that will be covered first I will give you an introduction of what if the digital image processing and then we talked about the origins of the IP and then we talked more about some of the applications of digital image processing then some about the fundamental steps that are involved the different components in any VIP system these

**1:23** · basically wraps up the first chapter of the book and for the second chapter we have some introductory material on the elements of visual perception how the light and the electromagnetic spectrum are defined and categorized and then finally a little bit a little bit about image sensing and acquisition and finally sampling and quantization of real world into digital images so the

### What is Digital Image Processing (DIP)?

**1:58** · first question that you might ask is what is digital image processing and the answer to that is we need to first define the image itself so an image you can consider that the two dimensional two dimensional function f of X and y with X&amp;Y being the spatial

**2:18** · coordinate and F at any pair of coordinate X and y is considered the intensity or gray level of the image at that point so this is the general definition of an image and in this general definition x and y or can be both continuous or discrete values the same is true for the value at any point

**2:48** · 2 so f can have any value from 0 to infinity but when x and y and the intensity values f or finite discrete quantity of the image if considered at digitally so digital image processing if the process if all the processes that

**3:11** · involve digital images by means of digital computers so you can say each digital image composed of a finite number of elements which are usually called pixel but our name to them to picture element image element or health but now the question becomes if this is

**3:35** · the definition of the digital image processing water its limit so if image analysis also visual image processing or more advanced techniques that are usually used in computer vision or all of them also part of visual image processing and the answer to that is yes and no so to better categorize different

**4:04** · types of processes that are applied to images we can have three different levels we have the low level processes in which both the input and output to the algorithm or images so some examples

**4:20** · can be noise reduction contrast enhancement image sharpening we can have mid level processes in which the input are usually images but the outputs or image attributes so example of these type of

**4:36** · processes or segmentation and classification of object and then we can have high-level processes in which given an image or a set of images the algorithm tries to make sense of the ensemble of recognized objects for example let's say if you have an image of a classroom so you have chairs there's students pan books so if you give this image to a high level

**5:08** · algorithm just like detecting each of the individual components and then putting all of them together can give you for example a description of what it sees and what you think the image is from so for example here the image can be of a classroom so the input is an image but the output is a higher-level

**5:34** · semantic description of what's happening inside the image so usually this whole image processing consists of processes hood input and output or images and also processes that extract attributes from the images so the high level processes are usually fall in the category of computer vision so as for the origin the

### The Origins of DIP

**6:03** · earliest application of digital digital image processing is in the newspaper industry when we had to transfer pictures for example a class across the Atlantic Ocean so before the

**6:25** · introduction of digital images and transmission equipment the process could take like days or even weeks but after that in the early 9

**6:41** · the time that required for this purpose reduce significantly to in order of hours in such techniques a specialized printing equipment coded the picture for transmission then transmitted them

**7:00** · across the ocean and then reconstructed at their receiving end and so early systems were only able to code images using five distinct levels of gray values by the end of the 1920s the capability increased to 15 levels so here you can see two examples of such images but that was the concept of

**7:30** · digital images what about digital image processing so as the definition that we had before digital image processing is basically processing the images using digital computer so this whole computer had to be invented to so we have the digital image processing so the foundation of

**7:53** · digital computers and dates back to 1914 there the concepts of memory that could hold programs and data and also conditional branching were first introduced then we had the invention of transistors at Bell Labs in 1948 then

**8:14** · common base business or oriented language or COBOL and formula translator Portland programming languages very invented in fifties and sixties invention of integrated circuits then operating system then microprocessor which had a processing unit as well as

**8:37** · memory and input and output components very mented in 1970s and then later on we had the invention of personal computers and large-scale trends large-scale integration and very larger scale integration in the 70s and 80s and in the present time we have computers that

**9:05** · fall under the category of ultra large scale integration because we were able to cram more and more transistors in the limited space that is available through in the CPU so in some senses visual

**9:24** · image processing and the advancement of computers go hand-in-hand an early example of application of the digital image processing date back to the Jet Propulsion lab which they use such algorithms to process image that were captured from the moon by Ranger 7

**9:49** · satellite around the same time the invention of computerized axial tomography or CAD or computerized tomography or CT very another application of digital image processing in their medical diagnosis to me when it

### DIP Applications

**10:12** · comes to the applications of digital image processing as you might imagine the area of our application are numerous so it's a good idea to be able to categorize the different areas so as

**10:27** · suggested by the book and followed here we focus this categorization on the source of of these images so they can be from electromagnetic signal acoustics ultrasonic electronic and computer generated images so let's talk about

**10:51** · electromagnetic signal devices for image processing brief introduction about electromagnetic waves and how they are defined so they are defined as propagating sinusoidal waves of their wavelength or a stream of massless particle traveling in a wave-like pattern for these two definitions depends on how you define the concept of

**11:18** · a photon whether you define it at the babe or as a particle so each method particle contains a certain amount of energy which we call it the photon and this energy is in proportion to the wavelength so the

**11:39** · equation for the energy of a photon if H F which in which H if the Planck constant and F is the frequency and as for the frequency it can be drive the ratio between the speed of light in the vacuum and the wavelength of a photon and wavelength basically is there the physical distance between the two the

**12:10** · two consecutive peaks in a sinusoidal wave so based on this definition the range of electromagnetic energy can be divided into several regions so at the higher end we have gamma rays x-rays ultraviolet then we have the range of visible electromagnetic waves and then we have infrared microwaves and radio waves which have lower amount of energy

**12:41** · so I've put the application on the left you see several application of gamma ray imaging so we have the bonus scanned we have the pet image or positron emission tomography we have satellite images of the sickness or Cygnus loop is a

**13:04** · celestial body and we have the gamma radiation from a reactor valve but these fall under the category of gamma ray imaging and for the x-ray I'm sure you are all familiar with different types of X images we have a chest x-ray we have an aortic angiogram we have a brain x-ray or brain CT image we have applications of x-ray imaging in electronics to be

**13:39** · able to detect faults and error in the circuit and then we have examples of x-ray imaging for night-sky applications you can take so this is an image the same Cygnus loop that we had in gamma-ray range this if the image in x-ray range then we have some applications ultraviolet imaging so for

**14:13** · example the first two are used in food and industry the one on the left is ultraviolet image of normal corn this is the corn infected by smut and then we have again the flag nose loop image in the ultraviolet range as for the visible

**14:33** · as for the imaging in the visible range you are familiar with all the concept for all the applications there the simplest one or ethically the images that we capture using are found every day also we have other types of imaging in the visible range using light microscope so we have different examples here for example this is an image of a

**15:09** · microprocessor using a light microscope this is an image of a cluster oh so this is for example an image of an organic superconductor and as you can see in the legend they all acquired using different levels of magnification we have example of imaging the visible range using satellite images to so diverse some examples are satellite images of the

**15:42** · Washington DC area the first three are captured in the visible range but we have the visible blue visible green and visible red and then the ones underneath are captured in the infrared range and as you can see in the following table each one is used to signify at different

**16:07** · types of features in the image for example we have some that signified the vegetation or the moisture content of the soil and so on and so forth this is another example of infrared satellite image of the continent of America which

**16:39** · correspond to the amount of light pollution in different areas of the continent on the right we have some example one example of microwave imaging or radar imaging of the mountains in

**16:59** · Tibet so this is usually used when we want to reduce the adverse effects of occlusions in satellite images for example if we are imaging the same area in the visible range the view will

**17:17** · probably be blocked by clouds but if we do the imaging in the microwave range we can eliminate the cloud in the image that we get as for examples of radio wave imaging MRI is a good example so you feed here to MRI examples so in MRI

**17:41** · what happens is that we have a very large constant magnet that helps to align all the not all but many of the molecules of hydrogen in the body along the axis of the magnetic

**18:03** · force of that large magnet then we excite different regions of the human body using radio waves and then we have detectors that detect that basically the behavior of the molecules when they want to go back to their original state and by recording that for the entire volume we can create a volumetric data using

**18:32** · the MRI machines and underneath you see one example of a celestial body the crab pulsar image in different ranges of the electromagnetic spectrum so we have the

**18:49** · gamma gamma range image then we have the x-ray the optical image the infrared and the radio baby imaging and as you can see these images are captured from the same object and they are perfectly aligned but imaging in different ranges of electromagnetic spectrum we can see different types of information as for the other types of sources that are used for capturing images I talked about

**19:23** · acoustics ultrasonic electronic and then computer-generated one so the one on top left is a cross-section of the seismic model under I think ocean that is used usually to detect reservoirs of all oil and gas top right these poor images or example of ultrasound imaging then underneath we

**19:53** · have example of scanning electron microscope which uses a beam of focused electrons to to basically quantify the the surface

**20:10** · surfaces our microscope examples and then finally in the left we have some examples of computer generated models or computer-generated images so there are

### Fundamental Steps in DIP

**20:29** · several fundamental steps in digital image processing that are usually used and/or discussed in the textbook for the course so after on deciding on the

**20:45** · problem domain we have the concept or the step of image acquisition and doing that requires a specialized tool so whether it's imaging in the visible spectrum or using a scanning electron microscope each one requires their own set of image acquisition equipment but

**21:08** · after we acquired the images then the next next step is usually image filtering and enhancement so as for image filtering you can think of noise reduction at one of the examples another example is to improve the contrast of the acquired images then we might have image restoration which mainly talks about image noise reduction but at the

**21:39** · same time cost about more advanced topics like blur or more moving artifact reductions then we might have color image processing especially if our images are in color or even if they are in grayscale image we can use pseudo

**21:59** · color image processing mainly because the human visual system is only capable of distinguishing between a few thousand of different intensity levels in the gray images but at the same time the human vision is very sensitive to changes even a slight changes in color so it can process like I would say hundreds of time different

**22:27** · intensity level if the image is in color so that's another a step that is usually considered we can have a wavelet and other image transform so one thing that I forgot to mention in the image filtering and enhancement we can divide the technique that we use here to either spatial processing or transform

**22:58** · transform domain processing so in the spatial processing what we do is that we work directly and the pixels of the image but in the transform domain processing they apply some transformation to our images and then we do whatever processing that we have in the transform domain so a very good example of this procedure is using Fourier transform that we will discuss

**23:26** · later on in this course wavelet transform you can see the you can see they are derived from a Fourier transform but they have their own processes as well so they can be much more advanced for image processing and wavelets are only one of the transform

**23:55** · that are usually used there are other types like curve LED different types of wavelets servlet and like so on and so forth which we don't cover them in this course then we have this step of compression or watermarking and then we have morphological image processing so these processes the input and output are

**24:26** · generally both images then we can have the different types of segmentation the segmentation can range from anything from point or edge detection to more advanced topics like a

**24:44** · region segmentation or object segmentation we can have feature extraction and then finally we can have image pattern classification so these techniques and generally have inputs of images but output our image attribute so in this course these three chapters won't be discussed and not all sections of the chapter that

**25:12** · are shown in white or also discussed because out of the topics are more suited for more advanced courses as for the components of a general digital image processing system we have the problem in domain we have the image sensors that are used for image acquisition and then we have some specialized image processing hardware and then the data after capturing is

### Components of a DIP System

**25:43** · transferred to a computer in in which case the processes are usually the common between all types of image processing techniques we may have hard copies we may have different image displays mass storage image processing software and then finally this data can be transferred to different locations using network or even put on the cloud

**26:11** · so these are limits processing usually involves this component the image processing software so now that we have a better understanding of what image processing is and different components of any image processing or digital image

### Elements of Visual Perception

**26:33** · processing system let's talk a little bit about the element of visual perception and to begin that we can talk about how the human eye so on the right you see a generic graph of the human eye it roughly resembles a

**26:53** · sphere with a size of around 20 millimeters and it has several components you have the cornea we have the iris we have the ciliary muscles that are connected to the lens and help to change the shape of the lens and then on the boundary we have the choroid we have the filler and then we have this internal part of the boundary that is

**27:24** · called the retina the retina itself has several sections we have the blind spot and we have the obeah too so lens is responsible for focusing the light under the retina ciliary muscle are responsible for changing the shape of the lens and then the retina contains

**27:51** · different types of light-sensitive cells that help us to basically absorb the light and see the image that we see so we have two types of cells we have cone

**28:11** · cells and we have rod cells so cone cells they are around 6 to 7 million of consult or I and they are very sensitive to color they are mainly responsible for the photopic or bright light vision and they are mainly concentrated around the deaf obeah we have three different types

**28:36** · of cone cells red blue and green cone cells which we don't talk about at this point then we have the rod cells that cover the rest of the retina and they are between 75 to 150 millions of rod cells they are sensitive to color but they are sensitive to low-level illumination so they are more responsible for the ESCO topic or dim light region here you see a

**29:10** · profile of the distribution of the cone and rod cells in the retina so if can see if we consider Fourier to be at zero degrees you see that the distribution of the cone cells a largely around the phobia while the distribution of Rod Souls Eve generally anywhere else and at

**29:41** · the blindest but which basically is connected to them a nerve that leave the eye we don't have either cones or rod cells so in regular camera the lens has a fixed shape and picked focal length and if you want to focus the subject we

**30:07** · do this by varying the distance between the lens and the imaging plane but in the human eye the distance between the center of the lens and the retina is fixed so to achieve the focusing capabilities the focal length is going to be changed and this uses those

**30:30** · ciliary muscles that I talked about in the previous slide and by changing the shape or the focal length of the lens we can achieve focusing capabilities in the eye as for the sensitivity of the human eye

**30:52** · to the changes of intensities human eye can attempt adapt with a very large range of intensity so this range of intensity is shown as a log they are measured in middle umber so the range is in the order of 10 to the 10 it goes from 10 to the negative 6 to 10 to

**31:20** · the 4 which is basically their clear limit but one thing that you should keep in mind that that the human eye is not sensitive to the full range at any given time so the way that it achieve this wide range is by subjective brightness so can it so you can say at any given time a smaller range II if their

**31:48** · sensitivity range of their the human eye so and adaptation happens usually based on their brightness level so the reason for this is that we have two different phenomena that affect the perceived brightness the first thing is that

**32:13** · visual system tends to undershoot or overshoot around the boundaries of regions in different intensities so to test that we can create sets of gray levels basically areas with exactly the same gray level and if you see a profile

**32:34** · of this figure and this is something this is the thing that we have but the perceived intensity will look like something like this so before moving from a torker to a brighter area we have one undershoot and one overshoe so these

**32:53** · are usually called these are called the mach band the other phenomena that controls the perceived brightness is that a region perceived brightness does not only depend on its intensity so this

**33:09** · is what is called a scientist imal taneous contra so to see an example in these three figures the the square in the middle in all the cases have have exactly the same intensity but because its surrounding have different intensity we perceive this circle this square darker than this one so as for the light and the

### Light and the Electromagnetic Spectrum

**33:37** · electromagnetic spectrum we talked about this before so in 1666 Isaac Newton discovered that when a beam of sunlight passes through a glass prism its decomposed into a continuous spectrum of colors that range from violet to Ray so the range of the

**34:03** · visible spectrum is around 400 nanometers to 700 nanometers with the smaller wavelength belonging to violet and the larger wavelength belonging to red so if you remember from one of the

**34:23** · previous slides there the energy was HC over F sorry HC over lambda so as you can see whenever we have larger lambda that means we have smaller energy and lambda is basically the distance between the two consecutive peaks of any sinusoidal wave so now that we saw how

**34:54** · the visible range of their spectrum can be derived from the electromagnetic spectrum it's good to see how we can perceive colors so what happens is that

**35:13** · the color that we perceive in an object or determined by the nature of the light reflected by it so based on that we can define two types of light we can have monochromatic or a chromatic light which is basically a light that is void of color represented or in only by its intensity or gray level and it can range from Lag to white and then we can have chromatic light which is past the

**35:44** · electromagnetic energy from point four three two point seven nine micrometer in the spectra in the electromagnetic spectrum but and the definition of light

**36:00** · by itself is not enough we have to distinguish between the radians the luminance and the brightness as for the radians we define it as the total amount of energy that flows from the light source and it's measured in watts then

**36:19** · we can have luminance which is the amount of energy an observer perceives from light source measured in lumens and what you can see is that the radiance and luminance they are not the same thing so for example the source can have

**36:40** · a radiance of let's say several what in the ultraviolet range but since the human eye cannot perceive the ultraviolet light the luminance is zero

**36:57** · or very very low and then finally we have the concept of brightness which is a subjective descriptor of light perception and basically impossible to measure because it's different between different different from person to person and it represents the achromatic notion of intensity so now let's see how

### Image Sensing and Acquisition

**37:27** · image sensing an acquisition works so images are generated by combination of an illumination source and the reflection or absorption of energy from the source by the elements of the scene so that was a mouthful but the basic idea is that we have some illumination source that is shining through a scene

**37:50** · and the and the reflection or absorption of that energy from the object that are in the same we can create an image so as you can see I put elimination and scene in

**38:08** · double quotes and the reason for that is these idea these concepts are very general so illumination can be from a source of electromagnetic energy like visible spectrum or from something completely different from an ultrasonic wave or from a beam of electrons or even computer generated the same is true for scene elements to that they can be

**38:40** · familiar object like a desk or a chair or they can be more exotic ones like molecules right formation human brain etc etc so to sense or capture images we

**38:56** · need to have a sensing element so the general graph for a sensing element is something like this we have some energy source or some illumination source we

**39:12** · have some sensing material and that sensing material basically converts this energy source into an electric signal that we can record and then show it as an image so this is a single same thing element we can put a bunch of these together to create a line sensor or even

**39:36** · better we can put them together to create an array sensor but and this is not something that can be done for all types of imaging or even recommended for all types of imaging and you see in a second why so even using a single

**40:00** · sensing element it's possible to create line or array images so this is one example of combining a single sensing element with a mechanical motion to generate it to the image or we

**40:17** · can use line sensing elements to create 2d images so here is an example of a line sensing element that is combined with a linear motion to basically a scan a bigger area and it's usually used in satellite imaging or another way is happening in CT machines that we have a

**40:46** · line sensing element that is placed around this circle and then we have the x-ray source so at any given time the x-ray source provides the illumination and on the other side we capture the amount of the x-ray that pass through

**41:09** · there the subject of the imaging and based on that we do reconstruction and we create images but perhaps the most familiar type of sensor which is used

**41:26** · for image acquisition is the one that is viewed in digital camera so in this case we have a scene we have an illumination source and we have this imaging system which basically captured the amount of reflection or transmission of the light

**41:49** · for the object within the scene so we have this internal image plane and then the output of this is a digitized image so now that we want to talk about the concept of digitization it's good to have a model for image formation so as

**42:14** · before we define an image of the function of special coordinate x and y and the value at each coordinate location eviler quantity which is proportional to the or to the energy radiated by a physical source so because of that the values for

**42:38** · f are non negative and they are finite because the energy soil source on the provides finite amount of energy so we can characterize this function by two components first we can have the illumination which is basically the amount of source illumination incident on the scene being viewed and then we have reflectance which is the amount of

**43:07** · illumination reflected by the object in the scene so given this definition we can define function f have to be the multiplication of a and are I can range anywhere between zero to infinity right

**43:25** · in theory but the reflection can only be from zero to one so if it's zero that means that we don't have any reflection and if it's one that means that we have a hundred percent reflection in the cases that the the light actually goes through the object for example in x-ray imaging we can exchange the the

**43:55** · Flecktones with transmissivity con function but the concept is still the same so now let's see how we can go from a continuous domain scene to a digital domain image so to do that we have to

### Image Sampling and Quantization

**44:18** · have two different processes first we have sampling which basically is digitally the end of the spatial domain and then we have the quantization which is that this duration of the fan so let's just look at look at the simple example here let's assume we have this scene with this object in a continuous domain and let's see what we see in the

**44:47** · line that is drawn between point a point a and point B so in this part of the line is in white region so that means that its intensity is high then we suddenly jump to the object we have a

**45:08** · slight variation in the intensity within the object and then finally after this point this part of the line is in the white region so we have highest amount of intensity one thing that you notice is that the since we are in a continuous domain there is always some source for

**45:32** · noise too so that's why the the profile that we draw here contains noise so sampling says that we have to divide this area into samples of fixed distance so these blue dots these are basically the samples that we get from the image

**45:57** · so this is the sampling port in which we digitize the spatial domain but what about the function domain for even though we did the sampling but the function values at any of the example can still have any value that it wants so the quantization basically tries to define some ranges and if a sample fall

**46:24** · within that range that is specific intensity value is assigned to that sample so this is the result of both sampling followed by quantization and we do this for all the lines within our images so doing that we go from this continuous image into a sample then quantized version of the image

**46:56** · so to put it in more mathematical equation we can assume that we have F of s and T as a continuous image function and bu sampling and digitization to create image f of X Y containing M rows and n color so the spatial coordinate values for x and y can change for X can

**47:23** · change from 0 to M minus 1 and for y I can change from 0 to n minus 1 and they are considered to be integer as for the quantization we can define L at the

**47:39** · number of intensity level that is usually represented as a power of 2 and the reason for that is that we are working with digital computers and digital computers work with zeros and ones in another word they work in base2 so it's usually common to represent the number of intensity level as a power of 2 for example if you are working with an 8-bit image we have 256 intensity levels that can change from 0 to 255 and this

**48:11** · is the equation that connected to L if the number of intensity level and K is the number of bits that are used to represent each intensity level so you can visualize each image in different forms you can visualize it as a 3d function with X&amp;Y being the spatial

**48:37** · coordinate and Z being the the function coordinate or we can show it as an image for x and y or till a spatial coordinate but instead of showing the VL the height of any given point we just show it with different colors or we can use a matrix view basically we see it as some number so this is the function view

**49:10** · of the image this is an equivalent view using matrix notation so these two are basically the same notation here we just showed each value as a function value of function f of x and y here we only showed the values themselves without consider them as samples of a function and we can show show it using x and y el

**49:45** · spatial coordinates to and putting each pixel a integer location in this coordinate system so if we considered if any pixel can be shown using two indices

**50:00** · we have f of X sorry F F of I and J I showing the the row number and J showing the column number and then based on that we can define for example the center of the image which is the floor of n over 2 and floor up and over 2 and the floor is basically there the Lord their small the

**50:27** · smallest integer number that is close to M over 2 so for example if M is 512 at the floor of 512 over 2 is 256 if M is 511 the floor of 511 over 2 is 255 so

**50:52** · now let's see what are the effects of spatial and intensity sampling and to do that we introduce the concept of resolution so we can have both a spatial resolution and intensity resolution so let's just see what happens with a spatial resolution so a special revolution is defined as the size of the smallest perceptible detail in it Mitch so what does it mean

**51:23** · it means that what is the smallest object in the image that can be inferred for a given resolution so we can measure it by the number of pixels per unit of distance so as you can see a special resolution has a physical meaning to it for how many pixels we have for let's

**51:52** · say every centimeter or every inch so a special resolution is dependent on the sampling rate so here you see some examples of exactly same images but with different spatial resolution so the image on top left is created using 930

**52:15** · dot per inch the one on the right is created using 300 dots per inch so the difference between the two Eve not that significant but still you can see the effect for example in this hand of the

**52:34** · clock you see that because of lower resolution there are some jagged edges when you reduce the spatial resolution even more the effect is more pronounced so this is an image that is created using 150 dot dots per inch and this one is an image that you created using 72 touch dot per inch so as you can see a lot of the content is not visible

**53:10** · accurately in this image for what about the intensity resolution intensity revolution is defined as the smallest discernible change in the intensity level and is usually measured in the number a bit used for quantitation so you remember before I talked about having an 8-bit image so in an 8-bit image that means that we have 256 different levels of intensity so now let's see what

**53:43** · happens in a medical image so this image is captured using 256 levels of intensity so this is basically an 8-bit image this one is created using 128

**54:01** · levels of intensity but the difference between the two is not as obvious but as soon as we have start decreasing the intensity resolution some patterns emerge that are not actually in the image itself so this is usually called a false contouring so for example in this image which is created on the evening sixteen different intensity levels you

**54:31** · see these contours that appear that are not visible in the original image and that is definitely an artifact of using low intensity resolution and finally if we go to two intensity levels there is basically no distinction between different parts of the image the only distinction is between brighter regions and darker regions so for example the background is completely dark now and the foreground is completely white now

**55:06** · so to summarize your both spatial and intensity resolution or the situation dependent spatial resolution depends on the number of samples we call it N and intensity resolution depends on the number of bits they call it K they each

**55:28** · called different types of artifact when we have two lower spatial resolution we end up having jagged edges online when we have two low intensity we end up with images that have false contour contour ef4 the sensitivity special resolution is more sensitive to the short variations that are common in

**55:55** · the images and for the intensity revolution it's more sensitive to the lighting variations sorry for their spatial resolution it's more sensitive to shape variation sorry I said short variation so now let's take a look at the three images so on the Left we have lift your metric detail but more lighting information and the reason for

**56:24** · that is that we have different shades of gray in different regions of the image for example if you look here we have start from a very bright shade to much darker shade or like it's obvious in different parts of the image as well the one in the middle we have much more geometric detail but less lighting information so you can clearly divide this image into a very bright background and very dark program and finally in the

**56:56** · last one we have most geometric detail because they're much more shape variations in the image but the lighting information is much less than than the previous two images so the question now becomes what would be a good digitization asking for these images is it possible to have a single scheme for the imaging or do they require different game so to answer this equation in 1915

**57:33** · 1960 they have done some experiments using human subject and they created a bunch of similar images in different intensity resolution and spatial resolution and then derived some subjective comparison between how human visual system person perceived quality in different images so

**58:06** · to make the conclusion they created graphs like this in which the horizontal line shows the the sampling and the vertical line shows their levels of intensity and then they created these pi so preference curves which basically shows images with the same quality judged by observers so for example here in the case of crowd image all the point

**58:39** · here represent almost the same quality so as you can see in this example different levels of intensity did not have that much effect on their perceived quality but on the other hand for example in the face example we see a

**59:06** · curved pattern so the conclusion was that images with more shape detail for example the crowd needed fewer intensity levels to achieve the same code as I said in this line you see that the quality here for example with n being 100 even with 2 to the 4 levels of

**59:32** · intensity is to judge equally to the images of the same sampling rate but 2 to the 6 levels of intensity on the other hand images with less shape detail for example the base image or more sensitive to the intensity resolution but less sensitive to the spatial resolution so this was the end of the

**1:00:03** · first lecture in the next lecture I'm gonna talk more about different types of intensity transformation and basic mathematics that is involved in digital image processing

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** - · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 2 - Basic Mathematical Operations and Intensity Transformations|Digital Image Processing - Part 2 - Basic Mathematical Operations and Intensity Transformations]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
