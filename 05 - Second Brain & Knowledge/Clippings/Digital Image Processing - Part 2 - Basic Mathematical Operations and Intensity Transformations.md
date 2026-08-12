---
title: "Digital Image Processing - Part 2 - Basic Mathematical Operations and Intensity Transformations"
source: "https://www.youtube.com/watch?v=SHdiFuiYKv4&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=2"
author:
  - "[[ASIP-Lab]]"
published: 2020-06-08
created: 2026-08-12
description: "Topics:00:30 Relationships Between Pixels17:36 Overview of Mathematical Tools for DIP58:10 Basics of Intensity Transformations and Spatial Filtering1:03:34 Basic Intensity Transformation Functions"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=SHdiFuiYKv4)

Topics:  
00:30 Relationships Between Pixels  
17:36 Overview of Mathematical Tools for DIP  
58:10 Basics of Intensity Transformations and Spatial Filtering  
1:03:34 Basic Intensity Transformation Functions

## Transcript

**0:01** · Welcome to the second lecture of the digital image processing course.

**0:06** · So, in this lecture I first talk about some of the basic relationship between pixels in an image, then I will introduce some of the mathematical tools that are commonly used for digital image processing.

**0:19** · Then we will go over the basics of intensity transformations and spatial filtering, and finally I introduce some basic intensity transformation functions.

### Relationships Between Pixels

**0:32** · So, let's talk about the relationships between pixels of an image.

**0:40** · So, the first topic that I want to cover is the concept of neighborhood of a pixel.

**0:47** · So, the first definition is the definition of a four neighborhood of a pixel.

**0:51** · So, let's just assume we have pixel PXY which is currently located in the center.

**0:59** · So, if you remember from the previous slide, we said that each image can be represented as a two-dimensional matrix.

**1:08** · So, based on that, we can define the four neighborhood of this pixel as the four immediate pixels next to the center pixel.

**1:19** · So, if this pixel has the coordinate of X and Y, the pixel right above it uh has the row number to be X minus Y and the column number to be Y.

**1:34** · This pixel that is to the right of the center pixel has the same row number, so their row number is going to be X, but the column number is going to be Y plus one.

**1:45** · So, these four pixels that are shown using these coordinates are representing the four neighborhood of pixel PXY.

**1:55** · In mathematical form, they can be defined as a set of X and Y for which the absolute value of X minus I plus the absolute value of Y minus J equals 1.

**2:10** · So, it's said that two pixels P and Q are four adjacent or four connected if Q is in N4 of P or P is in N4 of Q.

**2:23** · We can extend this definition to eight neighborhood.

**2:28** · So, when we do eight neighborhood, in addition to the four immediate uh neighbors, we have four additional pixels that are shown in the corners of this square.

**2:42** · So, for example, this pixel in the top left corner have the the coordinate values of X minus 1 and my Y minus 1.

**2:54** · And the one on the right bottom corner have the coordinate values of X plus Y and Y plus Y.

**3:03** · So, these eight pixels can be shown using these eight different coordinate values.

**3:11** · And in mathematical form, they can be defined as a set of I and J for which the maximum between absolute value of X minus I and Y minus J is equal to 1.

**3:25** · The same as before, two pixels P and Q are eight adjacent or eight connected if Q is in eight of P or P is in an eight of Q.

**3:39** · So, based on these definitions, we can define uh the concept of a digital path.

**3:45** · So, a digital path from pixel P in location X and Y to pixel Q in location S and T the sequence of pixel with coordinates X0 Y0 X1 Y1 all the way to Xn Yn for which the first set of coordinate is the coordinate of pixel P and the last set of coordinate is the coordinate of pixel Q.

**4:15** · And all the pixels in between are adjacent for I between 1 and n.

**4:22** · So the adjacency becomes important because depending on the type of adjacency that we are using, we can have different path between two pixels in the image.

**4:35** · So the length of the path is defined as the number of edges on the path. So you have to keep in mind that that we are here counting the number of edges and not necessarily the spatial difference or spatial distance between the two pixels. So for example here let's just say we have this pixel at the center and this pixel in the top right corner.

**5:02** · The if we are using let's say eight neighborhood, we can create a path directly from this pixel to this pixel.

**5:11** · So the length is going to be one even though the spatial distance is a square root of two.

**5:19** · If the beginning and end of the sequence are exactly on the same spatial location we say that the path is closed.

**5:32** · Because we can have different path going from one pixel to another it in some cases we may have some ambiguity in the definition of path.

**5:43** · For example in the same 3 by 3 image for pixel at the center and pixel at the top right corner if we are using the eight neighborhood, we can have two paths defined between the two. One is this direct path and the other one that is going through this top pixel.

**6:02** · So, but that is not the case if you're using the four neighborhood. So, depending on the application and the type of adjacency that we might have uh we can have different uh type of path with different length.

**6:19** · So, now let's talk about combination or union of some pixel that we call subset in the image.

**6:29** · So, assume that we have S as a subset of pixels in an image.

**6:34** · So, pixels P and Q are connected in S if there exists a path between them consisting only pixels that are also part of S. So, you can see an example here that this area that is shown with the red border

**6:53** · is the subset S and P and Q since both of them are contained in the subset and also any path uh that goes from P to Q uh only contains pixels that are inside the subset S, we say that they are connected.

**7:16** · For any pixel P in S, the set of pixels that are connected to it in S is called the connected component of S.

**7:24** · So, if it only has one component and that component is connected, the S is called the connected set.

**7:31** · So, you will see in the next slide how we can have multiple components in an image.

**7:38** · So, now let's assume R to be a subset of pixels in an image.

**7:43** · So, R is called a region within the image if it's a connected set.

**7:50** · So, if we have, let's say, two connected sets or two regions, R I and R J, we say that they are adjacent if their union forms a connected set. Otherwise, they are disjoint.

**8:05** · And as before, the definitions are dependent on how the neighborhood is defined. So, whether we are using a four-connected neighborhood or eight-connected neighborhood, uh we can have regions that are adjacent or disjoint.

**8:20** · So, you can see one example here. We have region I, which is basically the uh 3 by 3 matrix here.

**8:31** · And we have region J, which is the 3 by 3 matrix underneath.

**8:36** · So, these two, if we are using the eight-adjacent uh neighborhood, we can say their union forms a simple connected a single connected set because these two pixels that are next to each other are only connected if you are using an eight-connected neighborhood.

**9:00** · If you want to use the four-connected neighborhood, then these two regions are disjoint.

**9:11** · So, now let's uh suppose an image that contains K disjoint regions.

**9:16** · We call them we name them R K for K being from 1 to capital K.

**9:23** · So, we can define the union of all these regions.

**9:28** · And we can also define the complement of the union. So, all the points or pixels inside that union, we can call it as foreground, while all the points in the complement of the union can be called as background.

**9:48** · So, between the foreground and background, now we can define the concept of boundary.

**9:54** · But, we can define two different boundaries, inner boundary or outer boundary.

**10:01** · So, let's just go for inner boundary first. So, the inner boundary or border or contour of region R is the set of pixels in R that are adjacent to pixels in the complement of R.

**10:16** · So, basically, for defining the inner boundary, we are going from the pixels inside the region to the pixel outside. So, inner boundary contains only pixels that are adjacent to the background pixels, but they are part region itself.

**10:38** · On the other hand, the outer boundary of a region is the set of pixels in the background that have at least one neighbor in R.

**10:46** · So, on the figure to the left, you can see we have this image that is shown uh in this green rectangle. We have three disjoint uh regions. So, the union can be considered as the foreground, while all the regions, which are shown in white here, can be considered as the background.

**11:07** · Of course, depending on on the type of the problem that you want to solve, maybe R1 by itself is the foreground and the rest of the image containing R2 and R3 are part of the background, but that is application dependent.

**11:25** · And in the figure to the right, we can see the difference between the inner and outer boundary of this circular region within this rectangular image. So, all the pixels inside uh the inner boundary are also part of the region.

**11:44** · All the pixels that are part of the outer boundary are uh in the background.

**11:53** · So, now let's talk about uh some of the common distance measure that are used in uh image processing applications. So, before we do that, let's just uh list some conditions that any distance measure should satisfy. So, let's assume we have pixels P, Q, and S, each with their own respective coordinate.

**12:19** · So, if we want to define a distance function, this distance function should satisfy three different conditions. The first one is that the value of the distance function is greater than or equal to zero.

**12:34** · So, if it's zero if pixels P and Q are exactly in the same location, otherwise the value is going to be greater than zero.

**12:44** · The next condition is that the distance from pixel P to distance Q should be equal to the distance from Q to distance P.

**12:53** · Sorry, to pixel P. And this is very intuitive.

**12:57** · And finally, we have the condition the triangle condition, which means that the distance from pixel P to pixel S is less than or equal to the distance from pixel P to pixel Q plus the distance from pixel Q to pixel uh S.

**13:18** · And you can come to this conclusion intuitively if you consider a triangle that uh each corner of the triangle is one of the pixels P, Q, or S. If all the pixels are along a a straight line, in that case um we can have the equal the equality condition.

**13:48** · Basically, this part, the equal part.

**13:51** · Otherwise, um the distance from two pixels is less than the pixels that goes through the the third pixel.

**14:01** · So, now, based on these conditions, let's define some of the initial distance measure. So, the most straightforward one is the Euclidean distance between pixel P and Q, which basically defines a circle uh around pixel P.

**14:24** · So, it is defined as the uh x - u squared + y - v squared and under the uh square root of the second order.

**14:37** · So, if, for example, we have pixel P at the center, and we want to say, "Okay, what are the pixels that are uh in distance R of this pixel?" We can use the Euclidean distance to create a a circle around the pixel P, which is going to be at the center.

**14:59** · The next distance is the D4 distance, which is also called the city block distance, and its equation is defined as the sum of the absolute values of the differences. So, we have the absolute value of x - u plus absolute value of y v.

**15:17** · So, if we can show this, uh unlike the Euclidean distance, which shows a circle, this one shows a diamond with the center pixel has the distance of zero to itself.

**15:32** · These four immediate neighbors have a distance of one, and then the next uh level has the distance of two, and then the next level will would have the distance of three.

**15:46** · One thing that you can see is that the city block distance uh forms a diamond shape around the center pixel.

**15:56** · And for its own applications can be very useful, especially in image processing applications for which uh if you want to define a circle, some pixel might fall inside, while some other pixel might fall outside the circle. So, city block distance is very common in image processing application.

**16:26** · And finally, we have the D8 distance or the chessboard distance, which is defined as the maximum uh value between the absolute distances.

**16:38** · So, the maximum value of X minus U and Y minus V.

**16:43** · So, if you have uh the pixel at the center and its distance to itself to be zero, then the first level is all the pixels around that center in a square form. The next level will be a larger square with the size of two.

**17:02** · One thing that you might notice is that the same D4 and D8 distances were used before when we wanted to define the the neighborhood. So, if I go back to this uh slide slide which I defined a four neighborhood and eight neighborhood. You see that for definition of four neighborhood, I used the city block distance and for definition of the eight neighborhood, I used the D8 or chessboard distance.

### Overview of Mathematical Tools for DIP

**17:38** · So, now let's talk about another concept concept that is very useful in image processing application and that is the difference between element-wise versus matrix operation.

**17:52** · So, an element-wise operation involving one or more images is carried out on a pixel-by-pixel basis. So, let's just see an example of how this thing works.

**18:04** · Let's just assume we have two uh images that are each of size 2 by 2 pixels. So, this can be considered as the first as the first image, this can be considered as the second image. So, the element-wise product which is shown with this symbol is computed by multiplying each of the element with its corresponding element from the second matrix.

**18:31** · So, this is the result of the element-wise product of these two images.

**18:38** · On the other hand, the matrix product uh of the exact same images as before is a bit more complicated.

**18:47** · So, for example, to create the first element of the uh matrix product of the result, we have to calculate the multiplication of the first element of face first matrix and the first element of the second matrix plus the second element of the first matrix and the third element of the uh second matrix.

**19:12** · Or more accurately, the first row of the first matrix and the second row of So, I'm sorry, the first column of the second matrix.

**19:23** · So, this is very useful in image processing application.

**19:30** · Uh the element-wise operation, but you have to consider that for this to work, the two images have to have exactly the same size. Otherwise, you cannot perform element-wise operation. On the other hand, for matrix operation, as long as uh the number of columns in the first uh matrix is the same as the number of rows in the second matrix, you can produce the uh matrix uh multiplication.

**20:03** · So, now let's talk about linear versus non-linear operation.

**20:09** · So, we assume a general operator that produces an output image g of xy from a given input image f of xy. And we call this general operator h.

**20:22** · So, this operator actually performs on the image and then produces the output image.

**20:31** · So, this operator is said to be linear if it satisfies two properties. The first one is the homogeneity, which means that if we have h of f to be g, h of a, which is a constant multiplied by f, equals to a, the same constant multiplied by g.

**20:52** · The other condition that need to be satisfied for this operator to be considered linear is the additivity condition, which means that if we have h of f1 to be g1 and h of f2 to be g2, then it means that h of f1 plus f2 needs to be g1 plus g2.

**21:14** · So, these two conditions are summarized in this equation. As you can see, we have these two constant a and b and also f1 and f2.

**21:24** · And h of a f1 plus b f2 is equal a of g1 plus b of g2.

**21:34** · And if any uh operator satisfies this condition, we say it is linear. For example, a mean operator is a linear operator, while uh a max operator is not.

**21:48** · So, now let's just define some basic arithmetic operations that can be applied uh on images.

**21:56** · So, one thing that you should note is that these arithmetic operations uh can only be applied if the two input images have exactly the same size.

**22:06** · So, we can have the element-wise summation, the element-wise subtraction, the element-wise multiplication, and the element-wise division.

**22:18** · So, all uh these, as I said, are all element-wise operations and are performed between corresponding pixel pairs in f and g for x from 0 to m minus 1, basically uh representing the rows, and y plus 0 to n minus 1, which representing the column.

**22:39** · And as I said again, these are defined for input images of exactly the same size.

**22:45** · But one thing that you also should notice is that for the division, it's uh the user's responsibility to make sure that uh we don't have division by zero, otherwise the output result that we get is not going to make sense.

**23:04** · So, now let's see some examples of using these arithmetic operations.

**23:11** · So, for the first example, let's assume that we have an image acquisition system that for whatever reason may be the error of the imaging sensor or uh as some internal conditions of the imaging uh process itself, we have some zero mean uncorrelated noise that is added to any image that we capture.

**23:38** · So, for this, we can model the image that we uh acquire as G, which is the summation of a noiseless image plus some uh noise uh noise-only image. So, as uh I said, we consider this noise to be zero mean and also uncorrelated with the noiseless image.

**24:04** · So, that means that the amount of noise is not different for uh different pixels with uh various intensity values.

**24:15** · So, if that is the case, we can use uh image averaging between different noisy images, and that can help us to reduce the effect of noise. So, here you can see an example. Let's just say we have uh a telescope that is capturing noisy images of this uh celestial body or like galaxy.

**24:40** · So, if we have, let's say, K number of these images. Since the characteristic of the noise is random, that means that during each acquisition, we have different amount of noise added or subtracted from each uh pixel value. So, if we take the average of multiple of these, we can get to a noiseless image.

**25:02** · And the reason for that is uh if we uh find the average, what happens is that the expected value of the the average tends to go to the a noiseless image.

**25:22** · And the reason for that was that the noise uh image is uh is having zero mean or zero average. So, uh if we have enough samples, the positive values of the noise and the negative values of the noise uh gradually reduce the effect of each other and tend to go to zero.

**25:46** · If that happens, the variance of the uh pixels in the average image, so the variance of the noise in the average image is much uh smaller than the variance of the noise in the noisy image.

**26:09** · Another example of using arithmetic operation is when we use the difference operation for comparing between different images.

**26:19** · So, you saw it before, that's how having different sampling rate can introduce errors in our images. So, in these three images, we have some comparison. So, the first image is computed by um finding the difference between a 930 DPI image and a 72 DPI image.

**26:40** · As you can see, in the regions that are uniform in intensity, uh the amount of difference is very small, so that's why it's shown as black. On the other hand, in regions that we have uh edges, we have much more error. And if you remember from the previous set of the slide in the previous video, that when we have uh less sampling, that tends to create jagged edges.

**27:12** · And that is basically the effect that we can see here, too.

**27:17** · If we compare the 930 DPI image with the 100 DPI image, you can see that the error is still there, but it it's much less pronounced than the error that we got when we compared it to the 72 DPI image. And finally, between the 930 DPI and the 300 DPI, the error is even less than that.

**27:41** · Another application of arithmetic operations can be considered the their use in digital subtraction and geography.

**27:53** · So, the way it works is that at the beginning, we capture a reference image of um the human subject.

**28:02** · And then, we administer some contrast agent to the blood flow of the patient.

**28:10** · So, this contrast agent uh will move through the blood vessel.

**28:17** · And if we calculate the difference of this image with the original reference image, we can see that how uh the contrast agent is moving inside the vasculature. So, we can further enhance the difference by some technique that I will discuss later to get a much better representation of the vasculature uh in the patient.

**28:48** · Another example of arithmetic operation is when we want to correct the shading uh in an image. So, let's assume an image sensor that produces images that are modeled as the product of a perfect image times a shading function.

**29:05** · So, in this case, we can have our function our output image G to be the product of F, which is the perfect image, and H, which is the the shading that uh introduces artifact. So, here is an example of a chessboard image that is im- chessboard pattern that is image using such a sensor. As you can see, the intensities on the top left corner are much darker than the intensities on the bottom right corner.

**29:37** · So, if through whatever means we can get an estimate of this shading function, maybe for example, if we just uh a scan a blank piece of paper, using this estimate, we can use arithmetic operations, in this case, division, to create an artifact-free image.

**30:06** · So, a technical note that I have to mention here is that uh if you remember from before, when we quantize intensity levels, we said that we use a specific number of bit to represent the intensity range. What happens is that using any specific number of bits, we can only show a certain ranges of values. For example, if we are using eight bits, we can only show values between 0 and 255.

**30:37** · So, what happens if we subtract two eight-bit images?

**30:42** · In that case, the range can be anywhere from -255 to +255.

**30:50** · So, if we store this image using 8-bits, what happens is that all the negative values will be eliminated.

**30:59** · So, to uh avoid this, we should uh clip or scale the range of the intensities and uh put it back in the desired range that we want. So, to map the processed image to the desired range, which is usually from 0 to 255, for example, for a an 8-bit image, we can use this function.

**31:22** · So, this is the processed image, which uh the minimum value of the processed image will be subtracting subtracted from it.

**31:35** · So, that makes the minimum value to become zero. Then, we divide this image by Gmax, which is the maximum value of the intensity, and Gmin, which is the minimum value of the intensity. So, this whole process brings the range to uh between zero and one.

**31:59** · Now, if you want to change the range to zero and 255, we can multiply it by K, which here is 255. So, doing this procedure, we have an image that is now between zero and 255.

**32:17** · And we can easily store this uh image as an 8-bit image.

**32:26** · Another way of performing some functions on images is by using uh set theory.

**32:33** · So, set is called a collection of distinct objects. So, usually for defining any set, we need to have a sample space.

**32:43** · So, this blank space you can call it a sample space.

**32:47** · So, inside this now we can define a set of values to be contained in set A.

**32:54** · And if we define this set A, now we can come compute the complement of uh set A as A superscript C, which contains all the rest of the elements that are in the sample space, but are not in set A.

**33:16** · So, we can do the same for multiple sets.

**33:19** · And if we do that, then we can define the concept of intersection between two sets, which basically shows all the elements that are contained in both of these sets. Or we can define the concept of the union of the two sets, which is all the elements that are contained in either of the two sets. We can define the concept of set subtraction, which is all the elements that are in one set, but are not in the other set.

**33:50** · Then we can define the concept of intersection with the complement, which is equivalent to the subtraction.

**33:58** · And finally, we can even create much more complex uh relationships. For example, here we have sets A, B, and C.

**34:08** · And here we find the intersection of A with the union of B and C. So, these graphs are called Venn diagram, and they are very useful when we want to analyze or produce uh equations based on sets.

**34:27** · So, now you might say how we can use set operations to perform image processing task. So, let's just see a couple of examples.

**34:37** · So, one of the operations that we can apply to images is to find the complement of an image.

**34:47** · So, for an image to be considered as a set, we have to have three components.

**34:56** · The first two are the spatial locations, and the third one is the intensity value.

**35:02** · So, when we want to find the complement, finding the complement in terms of the spatial location doesn't make sense.

**35:10** · But, it makes sense in terms of the intensity value. Remember from before when we used X, Y, and the intensity value to show the image as a 3D surface.

**35:27** · So, if we consider that, we can define the complement of image A as set of X, Y, and K minus Z for all the X, Y, Z that is contained in the image.

**35:42** · So, we can consider the whole sample space as a cube for which X and Y are the spatial coordinates, and Z is the height of that cube.

**36:00** · So, the complement is all the intensity values that are not contained in the in the image for each pixel. So, for example, if a pixel is 10 in an 8-bit image, that means that the complement of 10 is going to be 255 minus 10, or 245.

**36:24** · Or, if the pixel is white, 255, its complement is going to be zero.

**36:32** · We also can define the union of two grayscale sets using this definition. So, the union of sets A and B in terms of images can be considered as the maximum of A and B. So, basically, the maximum uh of the intensities for each one of the spatial locations.

**36:55** · So, now let's see how this can be applied in real images.

**37:00** · So, on the left, we have the original image.

**37:03** · In the middle, we used a set operation for complement to create a negative of the initial image. As you can see, anywhere that the image was black is now completely white, and anywhere the image was white is now black, and all the intensity levels uh in between the two are reversed.

**37:26** · And the last column shows the result of the union of image A, this one, with the constant image. So, anywhere the intensity values were larger than that constant image, we keep those intensity values intact, but anywhere that the intensity values of the image was less than that constant value, we put the value of the constant image.

**37:55** · So, similar to set operations, we can have logical operations. So, logical operations deal with true or false variables and expressions, which means that we can apply them to binary images.

**38:10** · For which we consider the foreground to be all the pixels with value one and background with all the pixels with value zero.

**38:19** · So, a binary image can also be considered as a Venn diagram with regions of one valued pixels considered as sets. So, you can see some examples here. So, if we have B1 image as this background region and this foreground region, we can calculate the not of this image.

**38:43** · So, anywhere in the background is now white and anywhere in the foreground is now black. If we have two sets B1 and B2, we can calculate the and operation, the logical and operation at any pixel that is basically in both

**39:01** · uh set uh B1 and B2, we can define the or operation, we can define the and not operation, and finally we can define the exclusive or operation which contains any pixel that is in in either B1 or B2, but not in both.

**39:22** · And we can use a truth table to show this as well. So, here you can see an example of a truth table. So, for variables A and B, uh we can have four possible combinations ranging from 00 to 11.

**39:39** · So, and these are the three functions that three basic functions that can be defined on these two variables.

**39:50** · So, now let's talk a little bit more about the spatial operation.

**39:54** · So, a spatial operation work directly on the pixels of an image, and we can have three different types of a spatial operations that we will go through one by one in later slide. So, we can have single pixel operations, we can have neighbor operations, and finally we can have geometric spatial transformation.

**40:15** · So, for single pixel operations, they are usually used to alter the intensity of pixels individually using a transformation function T, which is defined in this form. So, this transformation function will be applied to any intensity value as the input, here shown as Z, and produces an output intensity value, here shown as S.

**40:44** · So, these are three different samples of uh single pixel operations that are applied to images. I will talk in more detail later on about them. But just so you know, this is the intensity transformation function for creating uh the negative or complement of an image.

**41:06** · This one is used for contrast stretching, and this one is used for thresholding an image.

**41:13** · Then we can have uh special operations that are neighborhood operations. So, for these, for any central pixel, we define uh a set of neighborhood pixels around the center. So, we denote it by S subscript XY.

**41:33** · And you can see an example here. We have the center pixel uh X and Y, and we define this neighborhood with M rows and N columns around it.

**41:43** · So, neighborhood operations generate an intensity value for the center pixel such that its value is uh a mathematical operation, for example, of all the pixels in that neighborhood.

**41:59** · So, after doing that mathematical operation, the new intensity value for the center pixel is computed and then placed uh the corresponding location in image J image J.

**42:14** · So, here you can see an example of image averaging. So, let's just say we want to uh do neighborhood operation for averaging an input image. So, this is the input image. We use this function to create this blurred image. So, any pixel in the result image is actually the result of averaging a neighborhood of pixels in the original image.

**42:43** · And then we can have geometric spatial transformation.

**42:47** · So, these one they do not work on the intensity. So, they do not change the intensity values.

**42:57** · However, they transform the spatial uh coordinate. So, there are two steps involved in geometric spatial transformation functions.

**43:08** · The first one is a spatial transformation of the coordinates and then later uh assigning intensity values to the spatially transformed pixel using intensity interpolation.

**43:21** · So, there are different types of geometric spatial transformations, but for now, we use the set of affine transformation, which can provide scaling, translation, rotation, and sharing.

**43:34** · Affine transformation are very useful because they preserve uh point, straight line, and plane within an image. So, the general formulation of affine transformation to create a new set of uh spatial coordinate is like this. We have X prime, Y prime, which are the new uh coordinates.

**43:58** · We have X and Y, which are the current coordinate, and we have this transformation matrix A, which is defined in this form using uh six unknown parameters.

**44:13** · As you can see here, we uh could define this function using only a 2 by 2 matrix, but that is not usually common. Otherwise, we had to have um a different uh transformation if you wanted to implement the translation. Right? But, to be able to contain everything in one single uh equation, we use this homogeneous uh coordinate system that give us this capability.

**44:49** · One of the very useful properties of affine transformation is that we can concatenate different transformation by calculating the product of their transformation matrices.

**45:01** · So, it can have a form like this.

**45:05** · So, if we only want to uh implement individual uh features, we can use each uh one of these uh transformation matrices individually. So, the first one, which is the identity transformation, basically probably gives the the same input image as the output. We can use a scaling and reflection using CX and CY.

**45:34** · If the uh two numbers are positive, uh we don't have reflection, but if the numbers are negative, uh we can have reflected images.

**45:47** · Then, we can have the rotation around the origin of the image, which is uh specified by the angle at which we want to rotate the image.

**45:57** · And the basic transformation is like this. We can have translation for which the translation along the X and Y directions are uh represented in the third column of the transformation matrix. We can have the vertical shearing and the horizontal shearing.

**46:19** · For example, if you want to find the general transformation function for both scaling and rotation, you can simply multiply these two together to create that general transformation function.

**46:37** · So, one thing that you should know is that only applying the transformation matrix to the spatial coordinate is not enough to create the a geometrically uh transformed image. So, this process is usually followed by intensity interpolation because when we rotate, for example, an image,

**47:00** · the in terms of matrices, uh we cannot have a rotated matrix because the grid that we use for image is always straight. It cannot be rotated. So, what we do is that after rotating the the image, we resample the image into the original uh matrix orientation.

**47:26** · So, there are several techniques for doing that.

**47:31** · The three basic ones are the nearest neighbor, the bilinear interpolation, and the bicubic interpolation. So, the nearest neighbor is the most straightforward one for which the pixel value the or the intensity value for any pixel that we want to interpolate is replicated uh by finding the closest pixel to it in the original grid.

**47:58** · So, for example, in this set of four pixels, if we want to find the intensity for uh this pixel in the middle, we find the closest pixel to it, and we replicate the intensity value of this pixel in this place.

**48:15** · For the bi- bilinear interpolation, we find the four nearest neighbor pixels, and then we try to solve for a, b, c, d parameters here. So, what we do is that we create a system of four uh linear equations, and we solve them to find these three parameters, a, b, c, and d.

**48:43** · As for bi-cubic interpolation, first we find the 16 nearest neighbors, and then we form 16 linear equations to find the 16 unknown coefficients here, shown as a of i and j.

**49:02** · So, here you can see an example of such application. So, this is the original image. This is the image after being rotated, uh say 30°.

**49:15** · So, this is the result of nearest neighbor interpolation. As you can see, the result has a lot of jagged edges.

**49:23** · But, if we use bilinear or bi-cubic interpolation, we can have a much smoother edge.

**49:35** · So, one thing that might be counterintuitive at this point is that you might think uh all the procedures need to be done in spatial domain because all the intensity values are shown in the spatial domain, while uh there are procedures that are better be done in the in a transformed domain. So, let's just briefly go over these.

**50:00** · So, some image processing tasks are best formulated in a transformed domain.

**50:05** · For example, in a Fourier domain. So, a general 2D linear transform of an image here shown T of U and V can be formed by this equation. As you can see, we have two summations, one going through the rows of the image, the other one going through the columns of the image, and then we have the original image f of xy, and then we have this R function, which is called a forward transformation kernel.

**50:39** · So, at this point I'm not going to go over the specifics of this R function. So, I'll just assume it as any general function.

**50:50** · So, this equation is evaluated for all the values of U and V.

**50:56** · We can recover the original image using the inverse transform of uh T of X and Y.

**51:06** · I'm sorry, it should be T of U and uh V using this function for which f of x and y is the summation uh over all the rows and all the columns in the transformed domain of T of U and V. This is a mistake. T of U and V multiplied by S, which is the inverse transformation kernel.

**51:30** · So, again, R and S at this point are generic uh functions, and I assume that whatever transformation that you are doing is reversible.

**51:42** · So, now we say that the forward transformation kernel is separable if we can divide it into two components that each only work on one of the coordinate system.

**51:59** · So, in this case R of X Y U and V is equal to R1 of X and U. Basically, it does the conversion for the uh hor for the rows to the transform domain multiplied by R2 which is doing the conversion for columns to the transform domain.

**52:24** · We say the kernel is symmetric if R1 and R2 are exactly the same.

**52:31** · So, the general approach for working in the linear transform domain can be summarized as follows. We have our input image in the spatial domain and we have our output image also in the spatial domain. But, in the meanwhile, we apply the transformation, we do the operation in the transform domain, and then we do the inverse transform to get back to the spatial domain. So, let's just see an example of how this thing works.

**53:01** · A very well-known example is when we use the Fourier transform for images. So, for the case of Fourier transform, the forward and the inverse kernels are shown using these uh complex functions.

**53:19** · So, I will go over them in much more detail uh at let at later later lecture of the course, but for now, let's just talk about them more visually. So, let's assume we have this image of the surface of the moon.

**53:38** · And as you can see we have this image corrupted by a sinusoidal interference that basically affects all the regions in the image.

**53:49** · So, you might say, "Okay, this is not redeemable because this interference is going through all the special locations between the and image." And you might be right if you were only working in the spatial domain, but if we transform this image using these two kernels to the Fourier domain, what we see is that this sinusoidal interference appear as two bright dots in the frequency domain.

**54:22** · So, what we do is that we define a mask with all the regions being white and only the two small points that are corresponding to the two pixels that are representative of the sinusoidal interference to be black.

**54:40** · So, by simply multiplying this mask to the Fourier transform of the image and then inverse Fourier transform, we can an image we can have an image that is completely artifact free. So, this is something that could not be done easily in the spatial domain, but can be done much more easier in the frequency domain.

**55:10** · One very useful way of representing images is as if we consider the intensity values as random variables.

**55:20** · So, if we consider that, we can define properties of any intensity level in the image. So, let's have V of I for I from 0 to L minus 1, basically for I as the range of the all possible intensity values of an image.

**55:39** · So, if we do that for any image, we can define the probability P of ZI, which is basically the probability of occurrence of uh intensity level ZI in the image.

**55:58** · So, the way that we define this probability is by counting the number of pixels for which we have uh the intensity level uh ZK divided by total number of pixels in the image.

**56:17** · So, this is very simple. The concept is very simple. But, as you will see later, it has wide range of application.

**56:27** · So, one thing from the probability theory is that if we sum up all the probabilities of a random variable, they add up to one. And that is going to be the case for uh images as well. Because what happened is that if I find the summation of all the probabilities, at the end, we are summing all the pixels uh divided by the total number of pixels within an image, which is going to be equal to one.

**57:01** · Like any other random variable, we can determine important uh properties of random variables using these probabilities.

**57:11** · So, we can define the mean or average of intensity in an image by the summation of individual intensity values multiplied by their probability.

**57:22** · We can define the variance of the intensities around the mean by finding the summation of the uh Z intensity values minus intensity minus the mean to the power of two multiplied by the probability of each intensity value.

**57:45** · And in general, we can define the nth uh central moment of the random variable Z about the mean by this equation. So, as you can see, this is a generalized equation of the variance. So, the zeroth moment is one, the first moment is zero, and the second moment is equivalent to the variance.

### Basics of Intensity Transformations and Spatial Filtering

**58:11** · So, now that we saw this, let us uh take a step back and see what we will cover in chapters three and four of uh this course.

**58:23** · So, we have different types of intensity transformation and spatial filtering.

**58:30** · But, these uh tasks can be done either in the spatial domain or in the frequency domain. So, the frequency domain will be covered in chapter four, so I'm not going to spend time on it now.

**58:43** · As for the spatial domain, this is the topic of chapter three. So, in this chapter, uh I cover two uh types of a spatial domain transformation. We have the intensity transformations, and then we have spatial filtering. So, for intensity transformations, we can have examples of image enhancement, but for and for spatial filtering, we can have the concept of image denoising.

**59:12** · So, I will get to individual uh applications and transformations uh in the following slides.

**59:26** · So, the first type of intensity transformations are the one that are applied on single pixels. So, the general formulation is something like this. We have S to be T of R. T is the transformation function. R is the input intensity and S is the output intensity.

**59:46** · As I said, these are done on single pixels.

**59:51** · And examples of this are threshold and contrast stretching. So, you see an example of a function that is used for thresholding and another example of a function that is used for contrast stretching.

**1:00:06** · So, for the thresholding, as you can see, any intensity value that is less than this threshold K will be mapped to zero and any intensity level that is greater than K will be mapped to one or uh white.

**1:00:24** · On the other hand, for the contrast enhanced contrast stretching functions, you can see we have this curved shape here. You will see later on how we can define different contrast stretching function.

**1:00:39** · So, these functions uh are independent of locations and on are and are only determined by the intensity values.

**1:00:49** · So, the procedure for performing these intensity transformation is that we check the pixel in a raster scanning method. So, basically, one by one.

**1:01:00** · We calculate the new value for each pixel. And then we update the intensity in the final result. And we repeat this procedure for every pixel. One thing that you should know is that we generally don't update the pixel values in the current image.

**1:01:19** · But what we do is that at the beginning of all uh our algorithm, we create uh uh similar size image. We either fill it with zeros or ones, and then after doing every operation, we just write the new pixel values in this new matrix, and we don't update it uh the original image, because that can have unwanted effect on the uh rest of the procedures.

**1:01:54** · Then we can have intensity transformations that are done in a neighborhood.

**1:02:02** · So, we you saw an example of it before when we used uh averaging. So, usually these neighborhoods are uh square shaped, so that means that the size of the uh neighborhood is the same along the horizontal and vertical axis.

**1:02:20** · And one example is intensity averaging.

**1:02:24** · Um the procedure is similar to the previous one. The only difference here is that for every pixel that we go over in a raster scanning method, we uh find its neighborhood first.

**1:02:38** · We do whatever operation that we want on the neighborhood, and then we update the corresponding location in the new image.

**1:02:49** · So, basic and intensity transformation functions are used when we are dealing with images that are either too dark or too bright, and because of these uh because of the side effects of these conditions, there are features that cannot be easily seen.

**1:03:09** · So, in the right graph, you see some of these intensity transformations that we will go over them one by one. So, the general formulation, as mentioned before, is S equals T of R.

**1:03:24** · And in digital images, S and R are discrete values, so we usually create a lookup table to define the function T.

### Basic Intensity Transformation Functions

**1:03:35** · So, let's go for the first example.

**1:03:37** · Uh image inversion, which is one of the simplest intensity transformation function that we can have. We already saw an example of using set operations.

**1:03:47** · So, to compute the negative of uh of an image, the transformation function looks something like this. S is equal L minus 1 minus uh R. So, L minus 1 is the maximum intensity range uh in an image. So, if the image is 8-bit, L minus 1 is 255.

**1:04:09** · And it's usually good for visualizing features when black areas on are dominant uh in size in an image. So, you see an example of a mammography image on the left. This is the original image.

**1:04:25** · As you can see, um the image is generally very dark. By using image inversion, we can create the image on the right, which is much brighter and um much easier to be analyzed.

**1:04:44** · Another basic intensity transformation function is the log transformation, which is used for enhancing or stretching dark areas in an image. So, the way the log transform function works is that it basically reduces the range for uh bright regions while increasing the range for dark So, in effect, it compresses bright areas in an image.

**1:05:16** · So, you know that the log of uh the log base 10 of 100 is going to be two, and the log base log base 10 of 10 is going to be uh one, right?

**1:05:32** · Uh and the log base 10 of one is going to be zero. So, as you can see, going from one to 10, uh you have a factor of 10. Going from 10 to 100, you have a factor of 10 again. But, in log transform, the difference between the two is going to be fact uh a difference of one. So, to avoid computing the log for very small values, which produce uh very large negative values.

**1:06:01** · So, you know that the log of zero is negative infinity.

**1:06:08** · We usually add one to the log function, and we have this constant that, depending on the application, we can choose its value.

**1:06:18** · So, one of the very useful applications of the log transformation is when we want to visualize the Fourier transform of an image. So, here you see uh uh a Fourier transform of an image, and the range of the values uh in this image is between zero and 1.5 multiplied by 10 to the power of six.

**1:06:44** · So, as you can see, the range is very wide. But, because uh this range is very big, uh the image appears very dark. So, in order to better visualize this image, if we compute the log transform, now we can see all the intricate pattern that were not visible in the previous image. Of course, this is mainly for visualization purposes.

**1:07:12** · So, we cannot use the log-transformed Fourier space to uh reconstruct the original uh image.

**1:07:21** · But, that is one of the capabilities of log transform, which uh help us better visualize uh Fourier transform of an image.

**1:07:34** · Another very useful uh intensity transformation function is the power law or gamma transformation.

**1:07:41** · You probably have heard about gamma gamma corrections uh uh before, especially if you were just simply trying to, let's say, adjust the brightness uh on your monitor, you probably have seen uh variable gamma. So, the way it works is that we have this general formulation for the gamma transformation. S = C, which is a constant, R, which is the intensity value, and then we have the power of R, which is gamma.

**1:08:13** · To avoid unwanted situation, it is common that we add a very small value to the value of R, but it's not always the case.

**1:08:28** · So, usually C and gamma uh are greater than zero.

**1:08:37** · Uh but, that is not always the case. It depends on the uh situation that you want to have.

**1:08:46** · One other thing that is usually common is that we uh scale the values of S and R between zero and one.

**1:08:55** · So, what happens with different values of gamma is that if gamma is less than one, we enhance the dark areas of an image.

**1:09:03** · If gamma is greater than one, we enhance the bright areas of an image. And if both of them are one, that is basically the identity transformation. So, S becomes R, which is not very meaningful.

**1:09:19** · So, by changing the values of gamma, we can create a wide range of functions that we can use and apply to different images.

**1:09:27** · So, now let's see some examples.

**1:09:31** · So, one of the applications of uh gamma transformation is in gamma correction. So, many image devices that are used for capturing, printing, or displaying images internally undergo a gamma intensity conversion process.

**1:09:49** · So, for example, in CRT devices, uh there is usually a gamma value of 1.8 to 2.5, which is applied to all the images that are shown. So, for example, if you have this image and you want to show it on a CRT image, this is what you actually see.

**1:10:11** · Uh the dark areas are much darker that you what uh you intend. So, what is usually common is that you apply a reverse uh gamma transformation to your image. And then, when you combine it with the internal gamma correction that is done on the monitor itself, now you have an image that looks more like what you intend to show.

**1:10:41** · Let's go for another example.

**1:10:43** · Uh in biomedical image processing, so, as you can see here, we have a biomedical image uh that is very dark. If you want to enhance the appearance of this image, uh we can use a gamma value of less than one.

**1:11:04** · And that uh causes the dark regions to be uh less pronounced in the image. So, the image the result the resulting image is uh much brighter than the original one.

**1:11:20** · So, this is the original image that you have. This is after using a gamma value of 0.6. This is after using a gamma value of 0.4. And this one is after using a gamma value of 0.3.

**1:11:37** · So, let's just go for a reverse example.

**1:11:40** · So, let's just assume we have this image which is very bright. And because it's too bright, it appears very washed out and detailed in bright regions are very unclear.

**1:11:53** · So, to correct this image, we can use a gamma value of greater than one. So, here you see three results that are created uh using gamma values of greater than one. This one is with a gamma value of three. This one is with a gamma value of four. And this one is with a gamma value of five.

**1:12:14** · So, in summary, we can have identity transformation, which basically gives whatever intensity value the that you have as the input to the output. We can have the negative or inverse transformation, which uh produces a negative of the input image.

**1:12:36** · We can have log and root functions.

**1:12:41** · These ones.

**1:12:42** · Uh which are used for dark images.

**1:12:47** · And we can have inverse log and power functions, which are used for bright images. So, gamma uh transformations are uh capable of performing both of these functionalities because depending on the the power or the value of gamma, we can either be under the identity uh curve or over the identity curve.

**1:13:17** · So, another type of uh intensity transformation uh functions which we call here generally as contrast and uh stretching, they can uh require more user input.

**1:13:33** · So, generally the functions that are used are either increasing or strictly increasing and that is to avoid avoid intensity artifacts. So, this is an example of a contrast and uh stretching function.

**1:13:52** · So, as you can see by changing the values of R1 and S1, R2 uh and S2, you can uh design different functions uh to be applied to your image. For example, if you have this raw image, if we chose R1 and S1 and R2 and S2 in such a way to contrast an image, this is to in enhance the contrast of an image, this is the result that we get.

**1:14:22** · But, we can modify these values in such a way that we get a thresholding function.

**1:14:29** · For example, if the S value S1 value is zero and S2 value is uh L minus one, that is when the contrast and stretching function is basically a thresholding function.

**1:14:44** · We can have intensity level of functions, too.

**1:14:47** · So, these are usually useful when you want to apply a certain function on a given range of intensity values. So, for example, if you want to have features of a of a specific region to uh stay in the same intensity while uh other pixels change their value.

**1:15:14** · So, let's just go for this example.

**1:15:18** · Here, the intensity values between A and B are shown uh using this value, and whatever is outside is shown using a different value.

**1:15:31** · Or this one, the intensity values in the range A and B are shown with a fixed value, while the range outside is basically unchanged.

**1:15:45** · So, you can see some examples uh here as well. So, on the left, we have uh an aortic image near the kidney area in the middle.

**1:15:56** · Uh we wanted to have the result of highlighting the blood vessel while making the other regions dark. So, this is a type of intensity level of slicing function that used that we used.

**1:16:10** · And in the third one, uh this is the result of keeping dark uh regions and blood vessel unchanged while darkening the other regions. Of course, there is no final answer, and it all depends on the type of application that you want to use it.

**1:16:35** · We saw that we can use different number of bits to show uh different levels of intensity in an image.

**1:16:43** · But, one thing that is interesting is that the location of these bits, or basically the weight of these bits, is going to be different. So, let's say if we have an image that use eight bit to show the intensity levels. So, the first, or the right most bit of the intensity value at each pixel is the least significant one because the weight associated with it is going to be two to the power zero, or one.

**1:17:13** · On the other hand, the left, or the left most bit of the intensity value at each pixel is the most significant one.

**1:17:25** · Why? Because the weight associated with it is two to the power seven, or uh 150 128.

**1:17:34** · So, what we can do is that we can decompose each image into eight binary images, each showing only one bit for each pixel.

**1:17:46** · And then, we can uh reconstruct the initial image using different uh sets of these binary images. So, let's just see how it works.

**1:17:59** · So, on the top left corner, we have our original image.

**1:18:04** · And the rest of the eight images that you see here are basic binary images that are created uh using the different digits of the binary number. So, this one is the bit plane one, which is the least significant bit. This one is the bit plane two, which is one level above the previous one. Bit plane three, bit level plane four, bit plane five, six, seven, and eight.

**1:18:33** · As you can see, when we go in this order, now the image features are more pronounced.

**1:18:46** · And the reason for that is that the more weight each bit had, the more effect it had in the final result.

**1:18:54** · So, the the smaller bits, basically the first bit, second bit, the third bit, if you count from the right of any binary number, they more look like noise, while the most significant bits, 8, 7, and 6, they contain more information.

**1:19:12** · So, now let's say if you want to compress an image using fewer number of uh bytes of data, what we can do is that we can uh decompose the image into its bit planes, and then use different uh number of bits for the reconstruction.

**1:19:40** · So, for example, here what you see is that we only used bits 8 and 7 to do the reconstruction of the original image. While the image looks a lot like the original image, but there are some fine details that uh are missing here. If we use bits 8, 7, and 6, now more images are visible, but the result still suffers from false contouring.

**1:20:08** · If we use uh bits 8, 7, 6, and 5, now we have an image that is almost indistinguishable from the original image. And if I go back to the previous slide, as you can see, uh the first the most significant bits, uh 8, 7, and 5, they contain most of the information that is uh used in the image.

**1:20:41** · So, in this lecture, I talked about different types of a spatial transformation function that we can have. So, in the next lecture, I will go in much more details about histogram processing and spatial filtering.