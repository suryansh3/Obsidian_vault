---
title: "Digital Image Processing - Part 4 - Spatial Filtering"
source: "https://www.youtube.com/watch?v=8xqmMVZH9qM&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=4"
author:
  - "[[ASIP-Lab]]"
published: 2020-06-22
created: 2026-08-12
description: "Topics:1:07 Review of Previous Lecture18:07 Smoothing (Lowpass) Spatial Filters42:21 Sharpening (Highpass) Spatial Filters1:05:43 Highpass, Bandreject, and Bandpass Filters From Lowpass Filters1:"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=8xqmMVZH9qM)

Topics:  
1:07 Review of Previous Lecture  
18:07 Smoothing (Lowpass) Spatial Filters  
42:21 Sharpening (Highpass) Spatial Filters  
1:05:43 Highpass, Bandreject, and Bandpass Filters From Lowpass Filters  
1:13:52 Combining Spatial Enhancement Methods

## Transcript

**0:00** · welcome to the fourth lecture of the digital image processing course in today's lecture I want to continue the talk on spatial filtering and then at the end I will give a brief introduction to fourier transform that will be

**0:20** · covered in much more detail in the following lectures so in today's lecture I will talk about the smoothing or low-pass a spatial filters I will talk about sharpening or high-pass a special filters I will talk about high-pass band reject and bandpass filters and how we can make them by only using low-pass

**0:45** · filter and then how we can combine a spatial enhancement method that we discussed so far so basically intensity transformation and a special filters all combined to give us the needed result for one example if you remember from the

### Review of Previous Lecture

**1:10** · previous lecture I mentioned that there are two main components in any spatial filter definition we have a neighborhood and then we have an operation that is defined in that specific neighborhood so let's just assume we have this image that is placed in this coordinate system along X we have the rows and a long why

**1:34** · we have the column so let us say we want to define a special filter in this neighborhood defined by nine blue squares so for this neighborhood we have a kernel in which its center is basically the middle pixel of the kernel

**1:57** · and this kernel has a bunch of weight associated with each one of the element of the the kernel so not only it defines the size of the neighborhood but also it find the ways that will be used to perform the needed operation so this

**2:22** · kernel is moved pixel by pixel across the image and at each picture in pixel location these weights are multiplied by the corresponding image pixel intensities and then they are going to summed up to produce the final result so

**2:45** · one thing that you should notice is that that is only one way that we can have spatial filtering in fact there are two ways we can have spatial filtering we can have linear spatial filters in which

**3:00** · the procedure as I described is basically producing some element wise multiplication and then summing all the results to get the final value for the response of the image to the filter but we can have nonlinear spatial filters in which the procedure is a bit different than linear ones so here we talk about median filtering which is a nonlinear

**3:31** · special filters and next in the following slide so let's just for now focus on linear special filters as I said linear special filters produce a

**3:48** · sum of product operation between an image and a filter kernel here we call the kernel W so the kernel by itself is an array which not only defines the neighborhood of the operation but also it has some coefficients or weights that determine the nature of the filter so depending on the values of the weight we can have different types of linear kernel the kernel is also called a mask

**4:19** · or template or a window so here you see an example of a three by three kernel so at any point X and Y in the image we can calculate the response of the image for dead pixel we denoted by G of X Y

**4:39** · and G of X I Y is the sum of product of the kernel coefficient in the image pixel that are contained in the area as specified by the kernel so as you can

**4:54** · see each one of these weight is multiplied by one pixel and then they are the all or sum together to create the final result for their image as we change the coordinate of X and y we basically move the center of the kernel so it goes over all the pixels inside the image it is very common in image

**5:24** · preserving application that we use kernel of outside dimensions in both x and y directions so if we have a generalized kernel of outside dimensions we can basically say the size is lowercase M by L or cos n and then we can represent m and n by 2 value to

**5:52** · integers a and B and then based on those the range of the values of M is mentioned to be from negative a to a and the range of the values for n is going to be from negative B to B so that way we can simplify the previously-mentioned equation in this very nice and compact form the metal called equation that we

**6:25** · signed the previous slide is what we usually called a correlation operation which you usually either showed using a hollow a store or a sphere called plus sign so here you see the same equation but only for a one-dimensional function so let us see how this can be done for a

**6:51** · one-dimensional image with a one-dimensional kernel so as you can see we have an image that has 8 values but it's only one dimensional and we have a kernel that has 5 values so the center

**7:09** · pixel for this kernel is going to be bit value 4 so since we want to find the response of this image to this kernel we have to basically align the center with the first pixel and then calculate the response and then move this one place to

**7:29** · the right until we get to the end of the image but the first thing that we notice here is that when we align the center of the kernel with the first pixel of the image there are two values that fall outside the boundary of the image that we have so in effect the calculation is

**7:51** · undefined for these two values - to avoid that one of the common ways is to 0 pad there the image so we don't have any undefined operation so since two elements of the kernel fall outside when we align the center with the first pixel we add two zeros and then we calculate the the element wise multiplication so we have 1 x 0 + 2 x 0 + 4 x 0 all the

**8:26** · way to 8 x 0 so the result for disk is going to be 0 so we put 0 here then we move the kernel one step to the right and then do the same the result will be 8 then the next one result will be 2 then 4 then 2 and then finally 1 and then when we move completely to the right we have two additional zeros at the end - so this is what is called a result of

**8:59** · correlation of this image with this kernel that we have one thing that you notice is that our image has only one value that is nonzero and this is generally and considered as to be a discrete unit impulse or the general definition for such function is mentioned here so Delta of X minus x0 is 1 if X is equal to x0 but it's 0

**9:32** · otherwise so for example here if we assume this as the first basically the 1 and 1 location the origin of the image so this function f is going to be Delta

**9:52** · of X minus 4 because it is 1 when X is equal to 4 otherwise it is 0 another thing that you notice is that when we you find the correlation between this discrete unit impulse and the weight what we get is basically a reversed version of the kernel at the location of the discrete unit impulse

**10:24** · but again the whole point is that this result is a rotated version of of the kernel so now let's say what if we want to have the exact same copy of the kernel so what should we do the way to do it is basically to rotate the kernel

**10:46** · 180 degrees before the correlation and then do exactly the same so we have this image we rotate a one-dimensional kernel 180 degrees vertically rotated around its center and then we get this rotated

**11:04** · kernel and then we basically follow the same procedure and the correlations or we place the center at the first pixel we realized that there are two values of the kernel that fall outside the boundary we add zeros and then we calculate the element-wise product and then some very low to get their final response of the

**11:32** · image to this pre rotated kernel so when we do that now we see that the convolution result is basically the exact copy of the original kernel at the location of the discrete unit impulse so pre rotating the kernel resolves in an exact copy of the kernel so now let's just see what happens if we have a 2d image for 2d images and to the kernels

**12:06** · the per thing that you noted is that we have extended these two equation for correlation and convolution to include two variables that are changing so the image that we have here is again a discrete unit impulse but it is in two dimensions or the definition that we have is Delta X minus X 0 and y minus y 0 it is 1 if X is equal X 0 and y equal

**12:33** · y 0 otherwise it is going to be 0 so if we assume the origin to be here so 1 1 location here this is going to be a Delta X minus 3 and y minus 3 because at location 3 and 3 the value of the function is 1 otherwise it is 0 and the kernel that we have the 3 by 3 kernel so

**12:59** · the first thing that we need to do is that we have to align the origin of the kernel which is its center pixel with the first element of the image that we have so if we do that we realize that there are some values of the kernel that fall outside the boundary or do to avoid undefined up relations with zero extend the image so

**13:26** · there are no values of the kernel that fall outside the boundary and then we basically repeat the procedure so you find a element-wise multiplication between each a kernel element and each

**13:43** · image pixel and then we find the summation we move to the next pixel we repeat the same we move to the next we sold with the page and repeat the same until we get to the end of the original image so if we do that for the correlation result as you can see we get

**14:06** · a replica of the kernel but the difference is that the kernel is now a flip in both horizontal and vertical direction so now let's do a similar thing as we did before so we pre rotate a kernel along both of its direction so we basically flip it around the horizontal direction and then flip it on the vertical direction to see what we get so this is the rotated

**14:37** · two-dimensional kernel and if we find the correlation between this kernel and this image now we have the result of the convolution which is the exact copy of the original kernel so by itself

**14:58** · correlation and convolution they may look almost identical and the pole point of rotating the kernel II may not be obvious but if we look at the different

**15:15** · properties of correlational convolution we realize that convolution even much more superior than correlation and that's why for linear spatial filtering we always use we generally use convolution setup correlation so let's go and check out the properties of correlation and convolution so the first property that

**15:47** · we want to discuss here is the commutative property so this is a property that is satisfied with the definition of convolution but it's not satisfied with the definition of correlation so if you find the convolution of F and G gives the same as combining the convolution of G and F so

**16:07** · that means that the order of the functions that are going to be convolved is not going to be important in another word it doesn't matter if you rotate the kernel or the image you still get exactly the same result but you cannot say the same thing about the image so you've got the correlation so that is

**16:30** · one good property of the convolution that is not present in correlation the other good property is the associated property which basically says if you convolve F with the result of convolution of g and h achieve the same as convolving edge with the result of convolution of F and G and that is a

**16:53** · property that is not satisfied in the correlation and finally we have the distributive property which says that you can distribute both convolution and correlation over summation this is something that is common between both convolution and correlation so because

**17:13** · of the commutative property of the convolution as I said it's not important whether the kernel or the image is pre rotated also because of both the commutative and associative property of the convolution you can perform multistage filtering by just simply convolving all the kernels first and then filter the image using the result

**17:41** · of the convolution of all the kernel also what we saw last time was that if we have separable kernel we can use this associative and commutative property to basically reduce

**17:57** · the computational time for the convolution significantly so this is something that will be discussed a little bit later on as well so now that we had a quick overview of what we did last time let's just total thing about the special filters but the first official filter that I want to introduce is the smoothing or averaging special filter which is used for reducing sharp transitions in density of the images so

### Smoothing (Lowpass) Spatial Filters

**18:31** · random noise also in introduces sharpen transitions in the images as well so smoothing or averaging can help us reduce noise to another application for exposing special filter leaves to reduce

**18:51** · aliasing in the result of resampling of images but this is something that will be discussed in much more detail in chapter 4 we can use the smoothing to reduce false contouring if you remember post contouring was the result of using not enough number of bits or intensity level to show an image so if you have an email that same and that is coded using

**19:23** · three bits and you want to convert it to an image that is coded using 8-bit you will see a lot of false contouring but by applying a smoothing espiritual filter you can reduce the effect of false contouring so there are two types of smoothing filters in fact there are more than two types of a smoothing filter but in general we have again

**19:51** · linear filters or non linear filter so in the class of linear filters we can have box filter kernels and low-pass Scotian will as examples and for the nonlinear filter we can have order statistic filter for

**20:11** · example a median filter is one of the order statistic filter so box filters are simple separable low pass filter kernels in which all the coefficients of the kernel are exactly identical throughout the whole neighborhood so if we have an M by n box filter the box

**20:41** · filter is basically a matrix side M by n with all the values being one but to reduce basically to not introduce any bias into the image we apply a normalization constant before the kernel

**21:02** · so basically we scaled down all these ones to not introduce any bias into the final result so for example here since we have a 3 by 3 kernel we want these values to add up to 1 and that's why we multiply the whole thing by 1 over 9 so if we had a kernel that was of size 5 by

**21:28** · 5 the normalization constant would be 1 over 25 so Y normalized the kernel because we don't want to introduce bias into the image so an area of constant intensity in the image should remain the same after filtering and preventing by a

**21:54** · steering filtering means that some of the pixels in the original and filtered images or s are staying the same but let us see how this filter can help us in smoothing an image on the top left corner we have the original image which is of size 1024 by 1024 pixels and then the rest of

**22:21** · these image that we have are a smooth using kernels of size 3 by 3 11 by 11 and then 21 by 21 one thing that you can see is that when you're working with a kernel of a smaller size the effect is minimal so there is not that much

**22:46** · distinguishable differences in terms of exposing from the first image to the second image but that will not be increase the size of the kernel of the box filter we see that we have more and more exposing to the point that there are some fine detail that are hardly visible in the emitter for example the pattern inside this square when we use a kernel size of 21 by 21 it's not visible or for example divs lowercase letter a

**23:19** · is hardly visible one other thing that you might notice is that when we apply the box filter there is this faint gray border that appear at the end after you finalize the result and this is as a result of zero padding the image to avoid the undefined operations when part of the kernel is outside the images boundary box filters are very simple and

**23:56** · suitable for quick implementation and they're very useful when we want to reduce the effect of exposing on edges but box filter bar no by no means or the only possible a smoothing kernel that you can have in fact you can have infinitely many different exposing kernels all with random weights and each one can have a different effect so

**24:26** · that's why we introduced here and Gaussian filter kernels so box filters are generally poor approximations of blurring characteristics are the lenses and box filters also favored blathering along the perpendicular lines because there is a dimensionality associated with box filters if you for example

**24:56** · rotate the box filter 45 degrees you don't get exactly the same filter as before so that means that they have preferences in terms of the directions of the edges or the features that they

**25:15** · have smooth to avoid these shortcomings we it's better to use circularly symmetric or isotropic kernels which means that no matter how much you rotate the kernel you still get exactly the same result so one of these types of kernels is the Gaussian kernels which is not only circularly symmetric but also

**25:41** · it is separable so the general definition for a Gaussian kernel is something like this we have the kernel with continuous variables s and T and the equation is defined as this we have

**25:58** · K which is a constant showing the strength of the kernel and we have e to the power negative x squared plus T squared over 2 Sigma X square so to signify this circularly symmetric a form of the kernel it is very common to replace as a squared plus d squared with R squared basically when you consider the center of the kernel at zero then we define a

**26:31** · circular neighborhood around the kernel or an hour around the center and based on the radius of that circle we define and distances and therefore we define the coefficients for the kernel so this simple figure shows values of the radius from the the center that we can use for defining different Gaussian kernels so

**27:06** · for example if we want to define a Gaussian kernel of size 3 by 3 or the pixel at the center the the value for R will be 0 for all the immediate neighbors the value for R will be 1 and for the diagonal pixels or the diagonal

**27:28** · element of the kernel devalue for r will be the square root of 2 so if you replace or for each one of these and you predefined the value for K and the Sigma you can basically come up with the wait for your corner so this is what is

**27:49** · called a sampling because the Gaussian function is a continuous function and cannot be applied directly to the image so because of that we need to sample it at integer spatial location and make a discrete kernel and as before since we

**28:06** · don't want to introduce any bias to the final result we normalize the kernel by dividing all the coefficients by the sum of the coefficients that are contained inside the kernel so for example here is an example of the Gaussian kernel of size 3 by 3 in which K is chosen to be 1

**28:30** · and Sigma is also chosen to be 1 so as you can see we have this normalizing constant right before the kernel which is 1 over the sum of all the values are weighed inside the kernel since Gaussian

**28:50** · kernel are circularly symmetric inseparable now you don't have to sample in two dimensions you can just simply sample along a cross-section that goes through the center of the kernel and then convert it to a 2d kernel by the procedure that I explained in the previous lecture so values of a Gaussian function at distances that are larger than three Sigma from the mean are very

**29:21** · very small so we can select the size of the Gaussian kernel to be max Six Sigma by Six Sigma so this symbol basically shows the the ceiling of the value inside of it so if we have that they

**29:44** · wanted if you want to define a kernel with Sigma of 3.5 the maximum size that we can have for the Sigma without having any significant effect since we eliminate some of the Gaussian value is 6 multiplied by 3.5 or 21 by 21 pixel

**30:12** · one other nice property of the Gaussian kernel is that the product and convolution of two Gaussian kernel is going to be also Gaussian so if you have F and G as two Gaussian functions with

**30:29** · their own mean and standard deviation the result of multiplication gives also a Gaussian kernel which has this mean and this standard deviation if we do convolution of the two functions again we get a Gaussian function that has this mean and this standard deviation of course I'm not going to go into detail of how these values or tries but you can easily do it yourself so now that we saw

**31:03** · how Gaussian kernels are defined let's just look at one example so here we again have the test pattern that we you or the box filters - but this is there a lot of low-pass filtering using a Gaussian kernel of size 21 by 21 with a standard deviation of 3.5 this one is the result of Gaussian filtering using a kernel size of 43 by 43 with a Sigma

**31:35** · value of 7 as you can see as we increased value of Sigma and consequently there we increase the value basically the size of the kernel we have much more blurring and one other thing to notice is that this blurring is much more uniform in all direction unlocked unlike the box filter which was giving preference to edges or features and that

**32:07** · are in perpendicular direction as for the size of the kernel we have these two results here one is acquired using a Gaussian kernel of size 43 by 43 with Sigma equals 7 and this one is the result of using a kernel size of 85 by 85 with exactly the same value for Sigma

**32:31** · so here the Sigma X event - and this is the difference image between these two filtered results what you can see is that the different image is all black which means that there is no significant difference between these two images so by considering Sigma we can have a good limit on their side of the the kernel

**33:00** · that we are going to use as well so there is no point of going any larger than 6 Sigma in the image of course it is not necessarily to stay at Six Sigma going beyond that going over 6 Sigma is not beneficial but going below 6 Sigma in some application it is used so now that we saw both box

**33:31** · filters and Gaussian filter being applied let's just talk a little bit about different types of padding that we can have so so far what we used was that we used zero padding to avoid undefined

**33:50** · operation but zero padding is not the only way possible for padding an image so in addition to the opening we can have mirror or symmetric padding in which value outside the boundary are obtained by mirror reflecting the image across the border and we can have replicate padding in which we replicate

**34:14** · the values for outside the boundary equal to the nearest image border value so you see the effect of different type of padding here too so here we have the result of filtering the test pattern using a Gaussian kernel of size 187 by one and determine with K being 1 and Sigma being 31 this one we use 0 padding

**34:44** · to avoid the undefined operation for the next one we use mirror padding and for the third one we use replicate padding as you can see in the video adding result we have this a gray border across the final develop but this is not something that can be seen for the mirror padding and replicate padding so usually in practice mirror padding and replicate padding or more common so as

**35:20** · you saw we can use a smoothing to basically eliminate or smooth out to fine details of the image so the level of this elimination can be specified by the size of the kernel that we are using so if you using a box filter the size of the kernel is directly related to the amount

**35:46** · of its molding that we get for de the Gaussian kernel the size of the kernel is one factor and the other factor is basically the Sigma of the Gaussian function so let us see one example of how the smoothing can be used for shading correction so this is an image

**36:06** · that we already saw before of this checkerboard pattern that is non uniformly illuminated so one thing that we said before was that to get this image corrected if we have a good estimate of the shading of the image we

**36:24** · can use arithmetic operations to basically get rid of that so one way that we discussed last time was that if we have access to the device that you'll use for scanning this image and then we scan a blank sheet of paper we can get a good estimate of there the shading but

**36:47** · what if you don't have access to their scanning device so can we use the original image to get a good estimate of the shading that is exactly what we did here so the original image is of size 2048 by 2048 and each square is up to

**37:08** · size 128 by 128 so the middle image is the result of applying a Gaussian kernel of size 512 by 512 and as you can see since the size of this kernel is very large and also the Sigma is very large we are basically eliminating the very fine detail in the image here will be there the grid basically the black and

**37:36** · white circles or sorry square that we have in the image so at the end what we get is a basically a highly exposed version of the original image to the point that the squares are not visible anymore but what is visible is the general shading of the image so be used arithmetic operation as we discussed before we can get an image that II that

**38:04** · is shading is corrected so that is one application of a low-pass filtering so now that we saw two example of linear spatial filtering let me look at one example of a nonlinear filter so order

**38:21** · statistic filters or nonlinear filters that work based on ordering or ranking of the pixels in the region that is encompassed by the neighborhood so unlike the linear filtering in which we produce a sum of product form here the kernel only specifies the neighborhood but we don't have any weight so what we do is that we basically order all the pixels that are within the area of the

**38:53** · neighborhood and then we replace their value for the center pixel by some ordering operation so one example the median filter in which it replaces the value of the center pixel by the median of the intensity values that are present in that neighborhood median filter it is very useful for reducing salt and pepper noise so the way that median is found is

**39:25** · first we order all the values of instant intensities in the neighborhood if we have several values that are the same they will be grouped together and then we find the value for which half of the intensity values are less than the median and half of the intensity values or greater than the median and that value is basically if the value that will be placed or the center pixel so

**39:57** · you see one example here here we have an x-ray image of a circuit board that is highly corrupted by salt-n-pepa noise and salt and pepper noise if generally different than the Gaussian noise so Gaussian noise is basically you can think of a additive noise but salt and

**40:19** · pepper noise it is a form of like multiple multiplicative noise to some extent or replacement noise because some of the pixel values are going to be replaced with very bright values and some of them will be replaced by a very dark value so in the middle you can see

**40:42** · the revolt of noise reduction using a 9 by 19 by 19 Gaussian low-pass filter with a Sigma of 3 and you can see the amount of noise is reduced but at the same time we still have no and there are much blaring in the areas of sharp features or edges in the image and that is something that is usually not desired

**41:10** · instead of media Gaussian filtering if we use the 7 by 7 median filter this is the result that we get and as you can see the image is almost completely noise free and a lot of the shop featured or still preserve but you should keep in mind that median filtering even though 80 is very good for salt and pepper not it's not necessarily the best solution for all type of noise filtering on the

**41:42** · other hand you have to consider that Gaussian building is one example of this mode including not the only possible way so there are much more advanced filtering techniques that not only can get rid of the noise but also preserve the details and sharp transitions in the images so only consider the Gaussian

**42:09** · filter and the median filter as two basic filters with and nice properties but they are not definitely the only type of filters that can have image processing so now that we

### Sharpening (Highpass) Spatial Filters

**42:25** · saw how smoothing or averaging special filters work let's just talk about sharpening or high-pass special filter so in sharpening filters we want to highlight or boosted intensity transitions within the image

**42:42** · so if we associate averaging or smoothing with the integration of the image then sharpening is associated with the facial differentiation so image differentiation helps us to enhance the edges and other discontinuities in the image like noise but and at the same time the emphasize of the areas of slowly varying intensity but before we go into much more detail let's just

**43:13** · quickly go over some of the properties of the first derivative and the second derivative of function so for the first derivative of a function the first derivative is zero in areas of constant

**43:30** · intensity it is nonzero at the onset of an intensity of step or ramp and it must be nonzero along intensity ramps as for the second order derivative it must be zero in areas of constant intensity it

**43:48** · also must be zero along intensity ramps but it must be nonzero at the onset and end of an intensity a step or rat so now let since we saw the property let us see how it works in images so for digital functions the derivatives are usually

**44:08** · defined in terms of differences so the first order derivative are the 1d function in the difference in a difference form is defined like this so derivative of F with respect to X equal f of X plus 1 minus f of X so in essence

**44:27** · for location X what we do is that we subtract the intensity value of its next pixel and the intensity value of that pixel and reason that we get the first order derivative as for the second order derivative it is similar to applying the same equation twice so to take an order derivative of f with respect to X is going to be f of X plus 1 plus f of X minus 1 minus 2 f

**44:58** · of X and here we use partial derivative because we want to have consistent notation when we go from a one-dimensional to 2 dimensional function so these two are defined here only for 1 dimensional function so let's just see how they perform when we apply them to this one-dimensional curve here

**45:22** · so you can consider this one-dimensional curve as a one-dimensional image that have three areas of constant intensity we have an intensity ramp and we have this intensity a step that is basically a sudden change from lower intensity to a higher intensity or vice versa but the important thing is that this step happens only within the length of moving

**45:52** · one pixel so let's just see how these two first and second derivative can be applied so the values of this 1 dimensional image are mentioned here so for the first derivative asset for any pixel we get the value for there the pixel in it try to it's right and then we subtract the value with the value at that exact pixel so for example for this

**46:22** · pixel for the first derivative we have 4 minus 5 which is negative 1 as for the its second derivative what we have is f of X plus 1 which is here 4 minus plus f of X minus 1 which is here 6 minus 2 f

**46:42** · of X so for the pixel it's going to be 4 plus 6 ten which is equal to zero and we do the same for all the pixels of the original image so when we do this this is the curve that we get for the first derivative and the second derivative so the first derivative is shown with this filled circles and second derivative is

**47:11** · shown with this hollow squares so now let's see what happened first for the areas of constant intensity so for areas of constant intensity else we saw and we saw before the first derivative is zero

**47:30** · the second derivative is also zero so let's see if this is satisfied so here's an area of constant intensity and as you can see both first derivative and second derivative or zero here's another area of constant intensity and both first derivative and second derivative are zero and here is another area of constant intensity and both first and second order derivative or zero we said

**47:57** · that for first derivative it must be non zero at the onset of an intensity a step or ramp so let us see if this is true so this is the onset of the intensity ramp and as you can see the first derivative is non zero here again we have this pixel for which

**48:22** · basically we have a change in the value of the first derivative so it goes from a non zero value to a zero value the same is true for this step as well so at this at this point right we have a

**48:39** · sudden change in the value of the first derivative here so as you can see here the value for the first derivative and also the second derivative is non zero and finally we said that the first

**48:55** · derivative is non zero in the area where of an intensity but the second derivative is zero in the area when intensity right so let's just see how it works so here we have this intensity ramp that you can see the first derivative is non zero in fact it's negative one because the slope of this line is negative one but the second derivative is is zero one interesting

**49:28** · thing that you might notice is that for their second derivative when we go from a higher intensity value to a lower intensity value we have a second derivative of a negative value but when we go basically depending on the direction now here we have a positive second derivative it is more interesting when we are going through a step so going through this step right before their step we have a value of positive

**50:02** · second derivative and right after death that we have a value of negative second derivative so because of this we have this zero crossing that can help us to locate the location of the steps or more generally image edges you will see example of how these are useful later on in the course so now that we saw how we

**50:27** · can define the first and second order derivative let us see if we can come up with ways to use them for image sharpening so for image opening using laplacian we are interested in creating an isotropic kernel or a bunch of

**50:45** · isotropic kernels with response independent of the direction of intensity discontinuity so one example is the laplacian operator which for two variables is defined in this form so Delta squared of F equals the second derivative of F with respect to X plus the second derivative of F with respect to Y so if we replace these two terms by

**51:13** · the definition that we for the second derivative using two variables x and y this is the equation that we get for dela flushing so Delta x squared of F equals f of X plus 1 and y plus f of X minus 1 and y plus f of X and y plus 1 plus f of X and y -1 -4 and

**51:40** · f of x and y so we can convert this equation into a kernel like this in which the value for the center or the origin of the kernel is negative 4 and all these immediate neighbors have a value of 1 the value for the corner will be 0 so that is what is called a laplacian kernel so as you can see the

**52:09** · kernel is isotropic for rotations of increments of 90 degrees so if you rotate this kernel 90 degrees either clockwise or counterclockwise you can get exactly the same kernel and that's why it's called isotropic but only for rotations are increments of 90 degrees but what if we want to incorporate the diagonal directions too so simply what we do is that we apply the same equation

**52:41** · for the diagonal direction as well and then we incorporate those weight into the kernel so if you do this the kernel that we end up with has a negative 8 at the center and all one's around the dissenter what if when the negative sign

**53:04** · is used for second derivative and that is something that sometimes is common to so basically it looks as if we multiply these two kernel with a negative sign so by themselves they are not going to be important but they become important when we want to combine a laplacian filtered image with an image so this is something that we need to consider when we want to combine

**53:35** · several images so by themselves having these like either positive or negative does not matter that much but one thing that you should notice is that the coefficients of each one of these kernels sum to zero so the reason for that we don't want to introduce any bias in the areas of constant intensity

**54:01** · because if we introduce bias that means that the laplacian operator for the area of constant intensity is non zero which is not what we intend to have so now

**54:17** · that we saw how laplacian can be defined let's just look at a quick example so as i mentioned using laplacian we can get the fine details of the image so what we

**54:35** · can do is that we can combine the laplacian of an image with the image itself to basically enhance it fine detail so the equation that we commonly use for the final sharpened image is G of X y equal f of X Y basically the original image plus C multiplied the laplacian of the image so C is a constant that constant that controls the amount of additional detail that we add to the original image so let's just look

**55:09** · at an example this is a blurred image of the North Pole of the moon since we want to sharpen it first we calculate the laplacian using using this kernel here

**55:26** · then what we do is that we add this image using a value of C equals negative 1 because if you remember the value at the center here is negative 4 so since we want to add additional detail the value for see need to be negative one so after adding these

**55:49** · two images together this is the sharpened image that we get if we use the other kernel this kernel with the exact same coefficients of negative with the exact same value for 3 and negative 1 what we have is this image which is a

**56:11** · bit more sharpened because you can see from the previous slide the second kernel is isotropic two kernels two rotations of increments of 9 45 degrees

**56:27** · so it can preserve much more details in other directions as well so in general if we are using these two kernel for sharpening the image we use see values that are negative and if used these two cannot be you see values that are positive so we saw how we can use the

**56:51** · second derivatives in in the form of laplacian to sharpen the image what about the first derivative so the first derivative are implemented using the magnitude of the gradient so the gradient of two the image at coordinate X and Y is defined as a two dimensional column vector we have the gradient of F

**57:17** · or Delta F equals G of X and G of Y G of X or gradient in the X direction is defined as the derivative of X derivative of F with respect to X and G of Y or the gradient in the Y Direction is defined as the derivative of F with respect to Y so this vector point at the

**57:45** · direction of the greatest rate of change of function f at location X Y in another word this vector is perpendicular to the edge at that location so since

**58:01** · it's a vector we can have magnitude and also an angle so here we work based mainly on the magnitude part so the magnitude of this vector can be calculated by squaring the individual component of the gradient and finding the square root of that value so this is

**58:27** · going to be called the magnitude image we show it here by mm x and y and at each location it is basically there the length of the gradient vector at that place M basically shows the rate of

**58:48** · change in the direction of the deck radiant so there is a more computationally suitable approximation that is usually used in which mm M of x and y is approximated by the sum of absolute values of G of X and G of Y so

**59:10** · similar to laplacian we can use derivatives in their difference form and we can create appropriate kernels for computing the gradient so here you can see two different kernels we can have Robert colonel and we can have Sobel colonel so this is a generic 3x3 region

**59:32** · of the e of the image in which as Z values are the intensity values so these two figures are the Robert Cross gradient of gradient operators as you can see they calculate the gradient along the diagonal directions and then

**59:53** · we can have the so Sobel operators that calculate the gradient along the horizontal and vertical direction so use of any of these is very common in image processing application the way that we do is that we usually calculate the gradient using any of these and then if we want to create the magnitude we basically combine the two gradients into a magnitude image so one example of using

**1:00:28** · first order derivatives is for detecting defect in automatic digital image processing systems or let's just assume a system that is used to detect the effect in contact lenses so this is an image of the contact lens so that if

**1:00:53** · Pacific system is able to detect a defect much more easier if we provide the magnitude image so we have two defects here which probably are not visible that much so for that a specific system if it if it's more comfortable

**1:01:14** · using the magnitude image we can calculate the magnitude image by applying the Sobel operator or Sobel kernels in both horizontal and vertical direction combine them to create a magnitude of the gradient and this is the result that we get and as you can see the defects that we have in the length are much more visible in this figure another technique that is

**1:01:43** · commonly used for sharpening an image is called unsharp masking so in this technique we can subtract an unsharp or a smooth version of the image from the original image to create a mask to sharpen the image with so let's just look at this one dimensional example here we have this original signal that

**1:02:08** · is basically constant values in two region and intensity ramp in the middle so if you blur the signal we get a function of this form then if we subtract the original signals and blurred signal what we get is what it called a non short man as you can see in the areas that intensity or the the

**1:02:38** · derivative changes we have undershoot and overshoot so now if we sum this unsharp mask with the original image we get sharpen image so in mathematical form we have to first blur the original image so we go from f of x and y to f bar of x and y so we can use any of the smoothing kernel that we saw so far then

**1:03:09** · to create the unsharp mask we subtract this blurred version from the original image and then they add this one sharp Mac mask with coefficient here shown as

**1:03:26** · K - the original image so depending on the value of K we can get different results so if the value of K is 1 this is called unsharp masking for values of K greater than 1 the process is usually called high boost filtering so you see an example of this technique in the

**1:03:51** · following figure so here we see we have an original image of size six hundred by 259 pixels which is blurred in general so to sharpen this we use image blurring

**1:04:11** · using it 31 by 31 Gaussian low-pass filter with a sigma of 5 and this is the blurred version of the original image that we get by subtracting this blurred version from the original image we get the unsharp mask now if we sum this unsure path with the

**1:04:38** · original image we get this result which is the result of unsharp masking so for down short masking we use a value of k equal 1 we tested with a value greater than 1 here in the last bigger the value of K is 4.5 and this is what is called a

**1:05:01** · high boost filtering as you can see if I go back a little bit since here we have and both negative values and positive values it is possible that after summing these two images the unsharp math and the original image we go out of bound of the possible value that we can use for the image so especially for the region in which the values may be negative we end up with these dork halos around the

**1:05:34** · edges so the value of K needs to be modified according to the result that we desire even though we haven't talked about Fourier transform yet there are some great insight that we can get if we have a good knowledge of the fundamental

### Highpass, Bandreject, and Bandpass Filters From Lowpass Filters

**1:05:57** · properties that connect a special domain and the frequency domain and the insight can help us understand how filtering works in general so a special and frequency domain linear filters are usually classified into four broad categories we have low-pass filters like we saw in smoothing filters either box

**1:06:23** · filter or Gaussian filter we can have high-pass filters like we saw in laplacian or gradient filters and we can have bandpass or band reject filter the

**1:06:41** · last three types can be constructed using low-pass filter so Fourier transform is used to go from the spatial domain to the frequency domain in effect for a transpose and

**1:06:57** · transform the compose of the signal here image into it's consisting the frequency component so there are two fundamental properties that connect a spatial domain and the frequency domain the first one is with regard to convolution so convolution in the spatial domain is equivalent to multiplication in the frequency domain and vice versa so that

**1:07:25** · means that if we have the convolution of two signals in the spatial domain the frequency domain that is equivalent to multiplying these two signal more specifically multiplying their Fourier transform on the other hand if we have convolution of two Fourier domain signals it is equivalent to

**1:07:50** · multiplication of them in the spatial domain the other property is with regard to the impulse function so if we have an impulse function of amplitude a in the spatial domain it is going to be a constant function of value a in the frequency domain and vice versa which means that if we have an impulse function of amplitude a in the frequency domain in the spatial domain its

**1:08:20** · transform is going to be a constant function of venue a so now that we saw those two fundamental properties let's just see how we can build high path band reject and bandpass filters from low-pass filters so before getting to the equation let's just quickly look at these figure on the bottom so in a

**1:08:49** · low-pass filter what we have basically is two region 1 region is the pass band and the other region if they stop at so a low-pass filter basically any frequency component that is inside its passband and it stopped any frequency component that is in side their stop and so now that we have this you can see the connection between the low pass filter and the high pass filter

**1:09:22** · so in effect a high pass filter and a low pass filter in the frequency domain they are basically related through this equation so a high pass filter is one - a low pass filter in the frequency domain but what is it going to be in the

**1:09:45** · spatial domain so in the spatial domain we said that if we have a frequency transform that is constant it is equivalent to having an impulse function in their spatial domain and that is basically what we have here so this one is converted to a an impulse

**1:10:10** · function in the spatial domain so now let's just make it more complicated whatever the band reject filter so a band reject reject filter has to pass bands or any frequency that is below u1

**1:10:27** · or higher than u2 will be passed through the filter and any frequency that is between u 1 and u 2 will be stopped so now you can easily see that the pan reject filter is basically a summation of a low pass and high pass filter so the low pass filter has the frequency cutoff of u1 and the high path has the frequency cutoff of YouTube so in the

**1:10:56** · frequency domain the band reject filter is Lopez 1 and high pass - but this signifies that the cutoff frequencies of these two are different what about the bandpass so a bandpass filter is one - a band reject filter in the frequency domain again bandpass is one - a band reject filter and if we convert it into a into

**1:11:27** · the spatial domain we have Delta - the special kernel that eviews for a band reject filter of course more detail regarding the implementation will be discussed when we discuss Fourier transform in the next chapter but let's just quickly look at one example so here we see a sample test figure as you can

**1:11:58** · see we basically have a circle basically a build circle with some hollow circles around it and as you can see the width or the frequency of the circle changes

**1:12:15** · so the frequency is kinda equivalent to the distance between the peaks of these circles or as we go from the center to the end as you can see these distances become a smaller so in the frequency domain that means that we have a several component of different frequencies so here what we have is the result of

**1:12:42** · low-pass filtering so as you can see any frequency that is higher than some cutoff frequency is smooth while the lower frequencies are kept intact this is the result of subtraction of the original image with the low-pass filter one figure C sub figure C showed the result of a high-pass filter again you

**1:13:17** · see that these frequencies around the center closer to the center had lower frequencies and they are smooth out while the higher frequencies are are kept intact this one is the

**1:13:36** · revolt of having a band reject filter and finally we have here the result of a bandpass filter of course if we go into much more detail when we discuss Fourier transform in chapter 4 so we saw several

### Combining Spatial Enhancement Methods

**1:13:54** · techniques that are used for a spatial enhancement so basalt technique that only worked on single individual pixels to transform the intensity values to improve the contrast also with some special enhancement techniques that either a smooth or sharpened image so in general due to limited processing application we usually have to apply several of these technique to achieve

**1:14:28** · the desired result so here we can see an example of such act on top left corner we have a nuclear whole-body bonus can in which we want to enhance their skeletal detail the figure on top right

**1:14:47** · if the result of the laplacian operator by adding the laplacian to the original image we basically get a sharpened image of course since as we discussed before using derivatives and images not only

**1:15:07** · enhances the edges but also enhance the noise as well the result is a bit noisy to remedy this we just combine the result of the Sobel operator so here is the result of a gradient magnitude that is obtained by applying two horizontal

**1:15:30** · and vertical kernels of the Sobel operator and then calculating the magnitude of the gradient by summing the absolute values of the gradient along the horizontal and vertical axis then we s moves this Sobel

**1:15:50** · image or Sobel a gradient magnitude image by a five by five averaging box filter then we mask the result of the laplacian operator with smooth Sobel

**1:16:12** · image so to do that we basically multiply this image with the result of the laplacian and then finally we add this as smooth or like this masked version of the laplacian to the original

**1:16:31** · image as you can see here we have a much sharper image but with less amount of noise and finally we apply a power law based intensity transformation to enhance the image contract of course as you can see several of these technique

**1:16:51** · that we discussed in this chapter are used of course depending on different applications you may use different technique or different combination of techniques to get to the desired result that you want so before jumping into much more details about Fourier transform and processing the images in the frequency domain let us have a quick introduction on why

**1:17:22** · processing images in the frequency domain is very common so before I start let's talk a little bit about Fourier series and Fourier transform so any periodic function can be represented at the sum of sine and or cosines of different frequencies each one multiplied by a different coefficient so let's just say we have this periodic function by periodic function what I

**1:17:53** · mean is that this function is going to be repeated indefinitely so as you can see by looking at the function itself it is very hard to see if there are sine and

**1:18:09** · cosine function that can create this but if I use Fourier series Fourier series transform I notice that this function can be created by combination of these for sine and cosine function that we have here and this is the topic that will be covered in much more detail in chapter 4 but what about functions that

**1:18:38** · are not periodic so for those functions be used for you transform into the Fourier series so any function that is not periodic but have a finite area under the curve can be represented as the integral of sine and or cosines of different frequencies multiplied by a weighting function so to see why Fourier transform is useful let us quickly go back to the previous lecture in which we

**1:19:14** · saw how having a separable or non separable kernel can help us reduce the computational time so for an image of size capital n m multiplied by capital N and a kernel of M by n if the kernel is not separable we needed to have M and M and operations to find the convolution

**1:19:47** · of the image convolution of the image with a with the kernel we saw that if the kernel is separable then the number of operations is significantly reduced to this equation so now if we do the

**1:20:04** · same filtering in the frequency domain using password transform the number of operations is even lower so it's going to be 2 m n log 2 of M n so here in these two graphs you can see how much computational advantage we get if we use a fast Fourier transform

**1:20:28** · instead of just doing the convolution in the spatial domain so the first graph shows the computational advantage of FFT over non-separable a spatial kernels as you can see for an image of size 2048 by 2048 if we increase the size of the kernel what we see is that the amount of

**1:20:58** · computational time is going to increase but on the vertical axis what we show if the computational advantage so it means that let's say we have an image of this

**1:21:14** · size and we want to process it or convolve it with a mask of size 201 by 201 so if we do this in the Fourier domain as opposed to doing it in the spatial domain we gain over 900 times computational advantage but that means that we can do the same convolution in the frequency domain more than 900 times faster for the

**1:21:45** · separable kernel the amount of computational advantage is a bit smaller but in any case it is still beneficial to do large convolution in the frequency

**1:22:03** · domain as opposed to in their spatial domain so for example for this email for an image of the same size and a kernel of 200 by 1 by 201 if the kernel is separable if we do the calculation or

**1:22:20** · the cohoon convolution in the frequency domain we get a computational advantage of over nine times but that means that doing this procedure in the frequency domain is nine times faster then if we we do it in this spatial domain of course for our kernels of a smaller size you don't get

**1:22:44** · that much advantage for example if the kernel side is 11 by 11 and doing it in the Fourier domain is actually more expensive because the computation advantage is less than 1 so in the next

**1:23:02** · lecture I will talk about the preliminary concept that are used for defining a Fourier transform and Fourier series I will introduce Fourier series of periodic functions of one continuous dimension I will also talk about Fourier transform of functions of one continuous dimension then I go over the convolution

**1:23:29** · in the frequent Fourier domain or in the frequency domain and what is the relationship between the convolution in the frequency domain and the spatial domain and also I will talk about sampling and Fourier transform of sampled function

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 3 - Histogram Processing and Fundamentals of Spatial Filtering|Digital Image Processing - Part 3 - Histogram Processing and Fundamentals of Spatial Filtering]] · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 5 - Introduction to Fourier Transform|Digital Image Processing - Part 5 - Introduction to Fourier Transform]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
