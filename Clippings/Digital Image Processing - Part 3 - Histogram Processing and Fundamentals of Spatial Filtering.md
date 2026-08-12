---
title: "Digital Image Processing - Part 3 - Histogram Processing and Fundamentals of Spatial Filtering"
source: "https://www.youtube.com/watch?v=FwS-5Lyqf84&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=3"
author:
  - "[[ASIP-Lab]]"
published: 2020-06-15
created: 2026-08-12
description: "Topics:00:57 Histogram Processing07:33 Histogram Equalization38:05 Histogram Matching (Specification)57:57 Global vs. Local Histogram Processing1:02:26 Fundamentals of Spatial Filtering1:09:32 C"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=FwS-5Lyqf84)

Topics:  
00:57 Histogram Processing  
07:33 Histogram Equalization  
38:05 Histogram Matching (Specification)  
57:57 Global vs. Local Histogram Processing  
1:02:26 Fundamentals of Spatial Filtering  
1:09:32 Correlation vs. Convolution  
1:24:00 Separable Kernel Filters

## Transcript

**0:00** · so welcome to the third lecture of the digital image processing course in this lecture I will talk about some approaches for histogram processing and contrast enhancement as well as I will give you some introduction onto fundamentals of spatial filtering so the

**0:21** · topic that will be covered in this lecture or histogram processing in general then histogram equalization and histogram matching finally a little bit on local histogram processing then I will introduce you to the fundamentals of spatial filtering do a quick

**0:45** · comparison between correlation versus convolution and then finally concept related to separable kernel filters so let's just quickly go over the definition of histogram one more time we have introduced this previously in a previous lecture so let's just assume R subscript K for K from 0 12 minus 1 to

### Histogram Processing

**1:17** · represent the intensity values of an L level image f of X and y so if you remember from before we said that the number of level of intensity has a direct relationship with it with the number of bits that we use for representing an image for example in an 8-bit image we have 256 different levels of intensity ranging from 0 to 255 so

**1:50** · based on this assumption we can define the uh normal on normalized histogram of image F using the following equation H of R subscript K equals n of K for all the values of K when n subscript K is the number of pixel of the image with the intensity or subscript K so in effect we create some

**2:25** · histogram bins basically the subdivisions of the intensity of scale and then we count the number of pixels that fall within those histograms so the most straightforward way is to divide the L level image into L different histogram beam and then start counting all the pixels with a specific intensity

**2:51** · value and then populate this unnormalized histogram we can normalize this histogram by dividing there on normalized histogram by the total number of pixels in the image so if our image has M number of rows and n number of columns as shown here the normalized histogram which we call it P of R of K is defined like the equation

**3:22** · basically the histogram the unnormalized histogram divided by the multiplication of M and n which gives the total number of pixels within that image so in some sense you can think of this normalized histogram and the probability function that specifies the probability of any intensity value happening within the image so since we have this other

**3:53** · interpretation as well we can use the concept from probability theory to quantify and find the properties of this

**4:09** · probability distribution so one of the very useful properties is that some of the probabilities over the full range of the possible values or possible possibilities will add up to one and it

**4:26** · is something that can that you can easily verify by plugging the equation for the normalized histogram into this equation and then if you do the summation you realize that they add up to 1 so as I said the components of this function are the probabilities of intensity levels in the image so usually when we use histogram

**4:52** · we are dealing with two types of images either the image a low contrast or high contrast so in low contrast images the histogram has a very narrow intensity range and that is in general on the other hand high contrast image has a much broader intensity range so now the

**5:18** · question becomes how we can enhance enhance the contrast of an image since generally speaking more even distribution of the histogram is linked to higher contrast so it is very natural to assume that if the histogram is expanded to cover the full range of intensities the contrast is going to be improved in an ideal image you can say every intensity level corresponds to the same number of pixels so the concept of

**5:54** · the histogram equalization to works based on this assumption so here we have four different images of the same scene but with some problems with regard to

**6:10** · the histogram so the first one the image is relatively dark and as you can see in the histogram of the image all the intensity values are located in the lower half of the intensity ray and that results in a very general dark image at

**6:31** · the second image we have a much brighter appearance but the image looks very washed out so if you look at the histogram of the image you see that now the intensity levels are more located toward the bright side of the intensity range we have this image a low contrast

**6:56** · representation of the same scene and you can see here again we have another type of a very narrow representation of the intensity levels and finally we have this high contrast image and as you can see the histogram is much more spread out across the full range of the intensity value so the aim is to start

**7:22** · from any of these three low contrast images and create an image that resembles more of a high contrast histogram histogram equalization

### Histogram Equalization

**7:37** · technique fall usually under the umbrella of single pixel transformation that we introduce later so to begin with we can just assume a continuous case since the concept of histogram equalization can be mathematically proven in a continuous case it's not the same for a discrete case as you will see in later slide so let's just assume we

**8:07** · have a continuous range of intensity values we represent it with R and the range is anywhere from zero to L minus one and let's just have a transformation or intensity mapping function defined in this form as equals T of R or being the input intensity range and s being the output intensity range so we define some conditions on function T so one of them is that function T needs to be

**8:41** · monotonically increasing function in the interval of 0 and L minus 1 and other condition condition B is that the range of the value that this function produces should be exactly the same range as the range of input so as you can see P of our lies between 0 and

**9:09** · L minus 1 for any R which is between 0 and L minus 1 so this is an example of a monotonically increasing function so in different parts of this function we have different properties of example in this part and in this board as you can see it is strictly monotonic which means that there is a one-to-one correspondence between any pixel with input intensity

**9:40** · range and the output intensity rate so in these two regions the correspondence is one to one and is reversible but there are some ranges of values that you have a mapping of multiple intensity range to one single output range so since we have this we have to define

**10:08** · condition a prime which is used for functions that are a strictly monotonic which means that the correspondence is going to be one-to-one and reversible so

**10:24** · these three conditions each guarantees some useful properties of the transformation function condition a guarantees that the output intensity values will never be less than the corresponding input values that help us to prevent artifacts and any intensity reversal condition began T is that the

**10:48** · range of the output intensity is the same as the input image and if you remember from the previous lecture when I was talking about arithmetic operations done on images I mentioned that we when we do some I think on an image it is possible that the range of the intensity in the final image is different than the range of that intensity in the input image and to

**11:19** · remedy that we used either gripping or scaling so having conditioned be basically guaranteed that we don't have that problem anymore and condition a prime guarantee that the mapping function from R to s is one-to-one and reversible so now that we have these conditions on the transformation function let's just move forward with the continuous case of histogram Equalization so for this let's just

**11:54** · assume P R of R and P f of s being the probability distribution function or PDF of the intensity values in the two images that we have are being for the input image and s being for the output or the histogram equalized image so from probability theory which I don't go in

**12:23** · much more detail here if you are interested you can refer to the corresponding text for probability theory we conclude that if the PDF of the input image and the transformation function which satisfies the condition that I described previously if these two are known and if T are continuous and differentiable function over the range of values then we can calculate the PDF

**12:57** · of the transformed variable s and the equation for that calculation is mentioned here so P s of s equals PR of R multiplied by the absolute value of the differential of R with respect to s

**13:17** · or more specifically this is the inverse of differential love s with respect to or so but this is too general because we didn't expect by any properties on the function the transformation function so for the purpose of histogram equalization we want to have a PDF for the output image

**13:48** · that resembles a uniform distribution over the intensity right so let's just assume that this more specific function the transformation function and see if this function satisfies their requirement that we have for the output PDF so here we define s to be L minus 1

**14:16** · which is a constant multiplied by the integral of the PDF of the input image over the range from 0 to R and here we use this w parameter as the dummy integration variable so this is generally called the cumulative distribution function or CDF so now that we have this let's just see if we can find the probability distribution function of the output image so before

**14:52** · that let's just see if this transformation function satisfies the conditions that we have specified before so the first condition that we had was the transformation function needs to be monotonically increasing so let's just see if this condition is satisfied so first of all in this function we have L minus 1 which is a positive number so this doesn't have any effect on the the function then we have this integral that

**15:25** · is computed over the range from 0 and or and then inside the integral we have the PDF of the input image so as you know pdfs are always positive and if we are computing the integral since

**15:44** · integral is the area under the function since then previous is always positive this integral is going to be always increasing when we change the value of R from zero to its final value which is L minus 1 so this is transformation function did then satisfy the first

**16:11** · condition that we had condition a this transformation function satisfied that condition but not necessarily condition a prime because it is possible that

**16:28** · there are some let's say especially in the discrete case we have some probability values that or 0 and even though we increase their their range the output function does not increase but I will talk more about this later on when I talk about the discrete case so the other condition that we had was the

**16:57** · range of the output intensity should be exactly the same as the range of input intensity so to test that we can just replace the value of R with the minimum and maximum value in the range so if we have or to be 0 then we have integral from 0 to 0 of the PDF of the input image which is going to be 0 so for value of r being zero is becomes zero

**17:26** · elbow on the other hand if we put or have the maximum value possible between the intensity range which is L minus 1 then we have the integral from 0 to L minus 1 of the PDF PDF of the input

**17:43** · image and as you remember from one previous slide is then the integral of the probabilities over the entire range equal one so in that case this part of the equation equals one and then the maximum value of s will be L

**18:03** · minus one so as you can see when we change the value of R from 0 to L minus 1 the value of s also changes from 0 to L minus 1 so this satisfies the condition the two main condition that we had for the transformation function so now let's try to drive the PDF of s to

**18:30** · drive the PDF of f first thing that we need to calculate is the derivative of s with respect to R so this is pretty straightforward DF s over D of R is going to be the derivative of the transformation function with respect to R so in the function that we had we had

**18:52** · this constant which we can take out out of the derivative and then we will have this constant multiplied by the derivative of this integral function with respect to R and as you can see and you know from mathematics courses that the derivative of a function with respect to the variable or an integral function which is defined based on that variable is going to be the function itself so this derivative of the S with

**19:27** · respect to R is simply L minus 1 multiplied by the PDF of or so now that we have this we can easily replace this derivative into the equation that we had for the PDF of s so P of s P f of s

**19:46** · equals P R of R multiplied by the absolute value of the inverse of this derivative so if I simply compute the inverse and replace it here I will have P R of R multiplied by 1 over L my one pro4 since all the values in this equation are positive we don't have have to have their absolute value then the PSFS simplifies to 1 over L minus 1 and

**20:18** · as you can see this is a constant value which means that the PDF of s will be a uniform distribution so you can see the effect in this example we have this random but continuous PDF for the input

**20:39** · image that is spread over the full range of 0 and L minus 1 and after doing the equalization we end up with a uniform PDF for their output image so let's do a

**20:56** · quick example of how this can work using a different function so for this example let's just assume P R of R to be 2 R over L minus 1 squared for the range of our being from 0 to L minus 1 and 0 everywhere else again we can create the

**21:19** · transformation function using the equation that we had before which was L minus 1 the integral of P ro or from 0 to R and here we use W as the integration variable so if I replace this function within this range inside the integral these two value this is the

**21:44** · constant you can take it out of the integral also this is minus 1 s squared since its content you can take out and one of L minus 1 and L minus 1 squared one term will be cancelled out so the constant outside is going to be 2 over L minus 1 so now if we compute the integral of W DW it's going to be W

**22:12** · squared over 2 so if I replace value of or in that equation I get R squared over two and then if I replace W with 0 I get 0 so after all the calculation this is the transformation function that we will have R squared over L minus 1 so now let's just compute

**22:38** · a derivative of this function with respect to R the derivative of R squared with respect to R is going to be 2 R and then L minus 1 in the denominator it is a constant that will be unchanged so the derivative with respect to R is going to be 2 or over L minus 1 which means that the inverse of this function is going to be d R over D s equals L minus 1 over 2

**23:09** · or and then finally if I replace this function here in addition to the P R of R in the equation that we had for calculating PSFS or PDF of s we will end

**23:26** · up with 1 over L minus 1 as we did before so as you can see it can be mathematically proven that having a transformation function like we defined will give us a histogram equalized output so now that we saw how it works

**23:52** · for the continuous cade let's just reformulate the equation for the discrete case so there are some differences between probability for discrete values and probabilities like continuous function so for discrete values instead of probability densities and integrals we have probabilities and summation so let's just quickly review

**24:21** · the definition of the normalized histogram so let's just say we have an image which is of size M by and so M number of rows and n number of columns and based on that we can define there a normalized histogram in this form so the discrete transform function

**24:46** · that we use instead of integral now uses information but the concept is very much the same so s subscript K equals T of RK which is equals to the L minus 1 and the constant and the summation of the intensity values over the range from 0 to K and if I plug this function here

**25:15** · this is going to be simplified to this form L minus 1 over x N and the summation of the number of pixels that happen to have a certain intensity so this procedure is called a histogram equalization or histogram linearization transform so let's just see how it works in practice so let's go for an example

**25:45** · we have an example of an image which is 64 by 64 pixels and let's just say we are using 3 bits to represent the intensity values in this image so when we have 3 bits that means that L is going to be 2 to the power 3 or 8 possible intensity values the ranges from 0 to 7 so this is the table that

**26:16** · shows the normalized histogram of damage so the first column is basically the intensity values the second column is the number of pixels with that specific intensity value for example Wittington in terms of the value of 0 we have 790 pixels with that intensity and finally the last column shows the normalized histogram the image so now that we have this let's

**26:48** · just use the definition that we had for the intensity transformation s of K equals L minus 1 the summation from J from 0 to K of P P of R RJ so let's just

**27:04** · plug these values to this equation and find s of K for K from 0 to L minus 1 so for the first term we have is of 0 equals 7 which is L minus 1 multiplied by only P of R of r0 as you can see here we are calculating this summation over a range so if K is 0 we only have one term

**27:34** · here so it will be 7 multiplied by P of R of R 0 so 7 multiplied by 0.1 9 which is equal to 133 for SL 1 we will have

**27:49** · the summation of two terms because J changes from 0 to 1 so we not only we have the term for or 0 but also we have the term for or 1 so the end result will be 3.08 we can continue this until we get to K being 7 in that case the final value will be 7 because we will have 7 here

**28:19** · and then the summation from J equals 0 to 7 which is basically the summation of the probability over the full range which have I discussed before adds up to 1 so now if we do this transformation we realized that we are started from an image with 7 sorry with 80 intensity

**28:48** · values but they are all integers but on the other hand after the transformation now we have 8 intensity value youth that are not integer in fact there are fractional numbers so to be able to remedy this we need to round up or down

**29:11** · these numbers to their closest integer in order to have a digital image at their output to so the next step would be to round these values for s to the closest integer value in the range 0 &amp; 7 so 133 becomes 1 3.08 becomes 3 4 point

**29:38** · 5 5 becomes 5 and so on and so forth so now we have calculated their intensity values of the output image and basically the mapping from the input image to the output image so if you look closely here we have basically their intensity value for the input image and here we have the

**30:08** · intensity value for the output image so for example here if we have an intensity value of 3 in the input image that will be mapped to an intensity value of 6 if we have intensity value of 6 in the input image that will be mapped in the map to the intensity value of 7 at the output image so this is a graph of the input normalized histogram so as you can

**30:39** · see we have a relatively decaying curve but the aim was to have a more uniform curve at the output so based on the transformation function that we define this is the transformation function that we get so for example 0 will be mapped to 133 and it's shown here 1 will be mapped to 3.0 8 and all the way to 7 but

**31:09** · this is before rounding their their value after we round the value and draw the histogram the normalized histogram of the output image we have a histogram that looks more like this so you might say okay this is not a uniform as we expected because in the continuous case we were able to create perfectly uniform

**31:36** · histogram for the output image but you need to realize that when we are working with continuous functions there is \[Music\] inference infinite possible values that we can have for their function value but

**31:55** · on the other hand when we are working with digital images that is not the case we have a limited number of values that we can have for the intensity and they all must be integers and you will see the effect when we were doing the rounding operation as well that because of the rounding there were several intensity value that are mapped to

**32:25** · single intensity so for example we have five point six seven which is mapped to six but also we have three points so our six point two three which is also mapped to six and the same is true for intensity values that are mapped of seven two but the point here is that even though this might not be perfectly uniform but in comparison to the initial one it is more uniform so it is much

**32:58** · more closer to a uniform distribution because a histogram is an approximate PDF and no new intensity values are and created in the process it is very rare

**33:16** · to get a perfectly flat histogram in practical application and unlike the continuous case it cannot be mathematically proved that the discrete histogram equalization result in a uniform histogram and the main reason for that if the the rounding operation that we did is nonlinear but however histogram equalization is a fully automatic technique and it doesn't need any extra parameter to be defined so the

**33:51** · inverse transformation from s back to R can be defined in this form of course this is not 100% possible and all in all cases especially as you can see in the

**34:10** · previous slide that since several input intensity values are mapped to one output intensity value going back from this is not unique and the correspondence is not one-to-one so this

**34:29** · transformation satisfies the two initial conditions that we discussed only if all intensity levels are present in the input image or in another word none of the histogram bins of the input image or empty but again this is not something that you can guarantee for all the images that you want to process so to

**35:01** · summarize histogram equalization has the advantage of being automatic without the need for any parameters and it conceptually optimal even though in real

**35:18** · life applications there might be some limitation so now that we saw how histogram equalization work let us apply to the first few images that I showed you of images with low contrast

**35:38** · the first image is the image with a very dark appearance and as you remember the intensity values in the histogram are located primarily in the dark region of the histogram after applying histogram equalization we drive this curve one as

**36:01** · for the transformation intensity transformation function and their resulting histogram after Equalization is this which as you can see is much more uniform that initial histogram that we had it can be seen in the result of the Instagram equalization that now the image has much more contrast the same

**36:28** · happens for the image that was much brighter again after applying the histogram equalization we have a much more uniform histogram for the output image and the contrast is also improved

**36:47** · for the low contrast image in which the intensity values were only around a very narrow range in the intensity range that is possible we basically see the same thing but on the other hand for there originally good contrast image we don't see that much a difference in the histogram equalized and original image

**37:15** · as I said before here you see the curves that we came up with for the intensity transformation function so the first curve is for the dark image the second curve is for the bright image and the third curve is for the low contrast image that we have here and finally for

**37:39** · the image that is high contrast to begin with you see that the curve is very close to the identity line that we can draw from zero to this corner and there isn't sure that is that the image already had a very good contrast so even after histogram equalization and the appearance of the image does not change significantly so now let's talk

### Histogram Matching (Specification)

**38:08** · about histogram matching or histogram specification well you saw histogram equalization tries to produce a transformation function to generate an output image with a uniform histogram but that is not always ideal or needed what if you want to specify the shape of the histogram yourself so that is the topic for histogram matching which gives

**38:35** · you the option to specify the shape of the histogram yourself so again let's just assume the continuous case and then we go for the discrete case so for the continuous case let's just assume that we have an image and input image with PDF shown as PR of or that we want to transform to an image with PDF P Z of Z

**39:06** · so here PZ of Z is not uniform the general idea of histogram matching is to use histogram Equalization as an intermediate step for the process so let's first assume as a random

**39:27** · variable that is defined using the same transformation function as we did for histogram Equalization so basically using this transformation function we transform the input image width variable or to histogram equalized image with

**39:47** · variable s now let's do the same based on variable V so let's convert the output histogram that we want into a histogram equalized version using function G of Z but with their with a similar definition so for the input image what we do is

**40:15** · that we use P or of or and we use W as the variable of integration or the output image we use PV of Z and views we add the variable integration so now that we have these two we can combine them to find out what is going to be the transformation function from the input image to the output image so since s is

**40:48** · defined to be a uniform distribution these two equation can be considered equal so now we have G of Z equals s equals T of R so now what we do is that

**41:06** · we need to replace the value of Z based on OS and then based on R so from this side of the equation Z is going to be inverse function inverse G function of s and then s is T of R so conceptually

**41:29** · going from R to Z can be done by calculating this combined transformation function so we can summarize the procedure in these four steps so first

**41:47** · we obtain and the P of R from the input image basically we calculate the normalized histogram of the input image then we used a specified PDF of the output image PZ of Z to obtain the transformation function G of Z to go from the output image to the histogram equality image now in the third step we

**42:11** · compute the inverse transformation V equals G inverse of s which is a mapping from s to D and finally we obtained output image by first equalizing the input then for each pixel s in the equalized image we perform the inverse mapping to obtain the corresponding pixel in the output image so as you can see the procedure is

**42:40** · much more complicated than the previous one but as I said if you considered a histogram equalization as an intermediate step you see that by performing the histogram equalization on both the input histogram and output istagram now we get to a common ground and then we can use inverse

**43:04** · transformation of G to basically go pulley from the input image to the output image but in general finding the analytical expression for inverse of G is not a trivial task however in the discrete case this is not going to be a problem so now let's see how we can do this for that discrete variables so we

**43:31** · reformulate the continuous case for the discrete case so first the histogram equalized from the input image to variable s and that is done by using this transformation function for all the values of K from 0 to L minus 1 then similarly given a specific value of f of K for a value of Q which also Q changes

**44:00** · from 0 and L minus 1 and we find the histogram equalized version of the output histogram after doing that the desired value for Z of Q is computed from the inverse transform that is introduced here in practice there is no need to compute the inverse of G since we have intensity values that are into integer it is simple to compute all the

**44:30** · possible values of G using the second equation so these values are rounded to the nearest integer value and I've stored in a lookup table and then given a particular value of escape we look for the closest match in their table so to summarize

**44:50** · these are on the four steps that we need to take for histogram matching for discreet images first we compute the histogram P of P or a bar of the input image and then we histogram equalized it to the uniform histogram again we round the resulting values to the two integer

**45:15** · values within the range then we compute all values of function G of Z cube basically we histogram equalized the output histogram and around the values two integers in the range 0 to L minus 1 and store them in a lookup table the

**45:34** · third step is a bit more involved in comparison to the third step in the continuous case so the main difference is that we may have multiple correspondence so for every value of s K for K from 0 to L minus 1 we use the stored value of G from step two to find the corresponding value of Z Q so that G of Z Q is closest to s of K when more

**46:05** · than one value of Z Q give the same match so basically when we have multiple correspondent by convention we use the smallest value between all the matches and finally from the histogram estimation a specified image sorry we formed a histogram is specified image by mapping every equalized pixel with value

**46:31** · as k2 the corresponding pixel with value Z Q in the histogram a specified image and for that we use the mapping found in step 3 so now let's take a look at it and example and see how this thing can be done for this example we use the exact same histogram that we use for the histogram equalization example we have a

**47:01** · 64 by 64 image image which has three bits that represent the intensity values of the images so in this table on the Left we have intensity values the second column shows the number of times each intensity value appears in the image and then the third column shows the normalized histogram basically the probability of each intensity value happening in Danish for the output

**47:35** · histogram we are using the specialized value so this column shows the intensity values for their output histogram and Deve show the probabilities of each

**47:50** · intensity value happening in their output so here you can see the input histogram and output histogram has to figure so as you can see in the input histogram we have a relatively decaying Instagram but on the output histogram first of all we don't have any instances of intensity zero one and two happening and form is like a triangle for

**48:19** · intensity values from 3 to 7 so let's just follow the procedure and see what is going to be there it's the result of histogram magic the first step was to

**48:36** · compute the rounded histogram equalized values from the input image to a histogram equalized version of it so this directly fro follows from the previous example so we have s 0 that resulted in 1.33 and then we round it to value one we have it's one which resulted to evaluate 3.08 which we rounded to three

**49:06** · and then so on and so forth for the second step we do the same for their output histogram so we find the value for G of Z zero to be very 0 G of

**49:23** · Z 1 to be 0 G of Z 2 to be 0 and if I go back one slide you see that these three values or going or 0 so the summation over the range will also result in 0 and

**49:41** · then you follow that for the rest of the intensity values as well but again since these values are fractional but we cannot use fractional values in digital images will be round these to their nearest integer values so the first 3 will be round it to a value of 0 then the fourth value is going to be rounded to 1 and then 2 to 5 6 and 7 so now that

**50:14** · we have these two mappings then we need to find the mapping between SK and V of Q so the first three values of G or equal so it's not a strictly monotonic therefore condition a prime is violated

**50:33** · but given this we follow a step 3 of the histogram matching approach which states we need to find the smallest value of the Q so that the value of the cube G of Z Q is closest to FK and this is done for every value of s K to create the required mapping from s to V for example for s 0 being 1 we have G of Z 3 which

**51:03** · is 1 which is a perfect match which means that every pixel in the histogram equalized image histogram equalized input images value 1 is mapped to a pixel with value 3 in the histogram a specified image but that is not all straightforward for other values

**51:27** · because we might have a multiple correspondent and if you remember from the step by convention when we have multiple correspondence we use the smallest matching value so after doing that and this is their matching that we come up with so in the histogram equalized input image any value that is 1 now it's going to be matched to three any value that is 3 going to be managed to for a value with value 5 it's going

**52:00** · to be matched to 5 6 to 6 and finally 7 to 7 so as I said the final step is to use the computed mapping to map every pixel in the histogram equalized input image into the corresponding pixel in the newly created histogram specified in this so after doing that we can create

**52:25** · basically we can compute the new histogram of the image this table the middle column shows the specified histogram that we aimed for and the last

**52:41** · column shows the actual probabilities that we got as the process of histogram matching of course you can see it's not a perfect match but if you look at the shape you see that it's much more similar to the specified histogram than the input image 1 and there are several reasons for that first of all is that we have a relatively a small image to begin

**53:12** · with and second of all is that we have regions that or like intensity value that basically do not appear in the input or in the output image but overall using still graham matching we can define a specific histogram and try to match the histogram up or image into that a specified histogram here is

**53:45** · an example of how histogram matching and histogram equalization can produce different results so on the Left we have an input image and underneath that we have the image and histogram as you can see the image a very dark but also it

**54:09** · has very bright regions as well but overall the and the image is more dominated by dark and black region so now let's see how histogram equalization can improve this image so the image in

**54:25** · the middle is the result of histogram equalization as you can see the appearance of the image a much more brighter than the original one there are some details that were not visible for example in this religion because of the varied Tork appearance we cannot see

**54:45** · some of the details but in the histogram equalized version it's much easier to see some of the details but at the same time as we can see the image is very washed out and very bright so because the dark regions are much more dominant in size in the image the bright region

**55:10** · don't have that much of an effect in the histogram equalization process so you can see the transformation function in this figure that we have a very sudden jump right in the region that are very draw torque in the image and as for the histogram equalized the histogram is heavily shifted to the right so the overall histogram is now much

**55:45** · more uniform but at the same time since we have a very large dark area within the image the output of the histogram equalization is not ideal on the other hand on the right we see

**56:02** · the result of histogram matching so when we look at the original image we notice that the detail in the bright regions are very much visible but what if not visible that effectively is the details inside the very dark region so with the specified histogram we try to basically stretch the intensity values in the dark

**56:32** · regions while we keep the intensity value in the bright region almost not affected so as you can see here this is the specified histogram that we use as you can see we are basically extending the histogram in very dark region while

**56:52** · they're bright regions are almost identical to the original image so if you use this histogram these are specified histogram and histogram matching now we can get this result which is much more pleasing than the first and the second image not only the M features in both bright and dark regions or more beautiful but at the same time the image has a more natural

**57:26** · look instead of being all bright or look washed out and here you see basically they estimate the transformation function this is the original transformation function from the s to Z and this is the inverse of it and then here you see the histogram aged images histogram both histogram

### Global vs. Local Histogram Processing

**58:01** · equalization and histogram matching or consider global histogram processing method since pixels are modified based on the intensity distribution of the entire image so if you aim to enhance details over a very small region of the image these two techniques fail because the number of pixels in those small areas have a very less significant

**58:27** · impact in their global histogram so to remedy this what we can do is that we can devise transformation based on intensity distribution of pixel neighborhood so in effect we combine the single pixel operations with neighborhood operations to create local histogram processing techniques for this

**58:55** · we define a neighborhood size and then we move its sensor center from pixel to pixel in a raster scanning manner and at each location we perform histogram equalization or histogram matching and we find a new mapped intensity for the center pixel and we replace the previous intensity with that new intensity value

**59:21** · one thing that you should notice is that this procedure is usually not done on the original image in fact a replica of the original image is created and the processing will be done on that replica with based on the value of the original image because we are doing this process with pixel by pixel if we basically change the values of the intensities for

**59:49** · every neighborhood the neighborhood of or overlapping we basically ruin the result of the processing but one thing that you should know here is that since from every neighborhood operation to the next either one row or one column of the neighborhood changes especially when you

**1:00:15** · have one pixel translation between neighborhood you need to you don't need to complete the full histogram for that neighborhood what you can do is that you basically just update the previous histogram so you are working with an

**1:00:34** · updated histogram based on the calculation that you've done for the histogram in the previous day so let's just see an example of how this thing might work so on the Left we have an image which is a little bit noisy but also it have these black regions that also contains some very faint shapes inside of them so other than this one

**1:01:04** · this circle the rest of them the shape of the shape with a different intensity inside this black region is not that visible so this is the result of applying histogram equalization in its local form what you can see is that then noises are a little bit magnified and image is a little bit washed out much

**1:01:35** · brighter than the previous one but still the detail inside these regions are not that visible even though they are more visible than the original image so if we do a local histogram occur locally equalization with 3 by 3 neighborhood now you can see the details inside date and these dark regions much more effectively of course this is only for you to see how these procedures can be

**1:02:08** · done with weather globally or locally for a specific application there the size of the neighborhood the technique for each neighborhood can be defined differently at any other application so now that we saw how we

### Fundamentals of Spatial Filtering

**1:02:30** · can perform contrast enhancement using mostly single pixel intensity transformation function let's just talk about spatial filtering so there are generally two components in any spatial filter definition we have a neighborhood and then we have an operation that is defined on the neighborhood so let's take a look at this image so as you can see here we have the image of origin and then along the x-direction we have the

**1:03:02** · rows and along the y-direction we have the columns so this image is divided into certain number of pixels so as before we have M rows and n columns at any given point we can define a neighborhood of a specific size and this neighborhood has some weight associated with that so as for the neighborhood we

**1:03:32** · define a different kernel or a mask that we move across this image pixel by pixel and at any location we perform some operation so as for the origin of the

**1:03:47** · the neighborhood or the kernel we use the origin to be at the center pixel so it is very common to use kernel of out size in both dimensions because if we are using kernel of even side in each

**1:04:08** · dimension we cannot define a center center pixel properly we can define as a central point but not necessarily a certain pixel so here you see an example of a 3 by 3 neighborhood and for each one of them as I said before we defined a weight that is associated with that

**1:04:32** · location in colonel so now let's say we apply this colonel on to this region of the image so generally if taking me we can have

**1:04:48** · two types of operations we can either have linear operations or non-linear operation or linear operation one example is averaging and nonlinear operation one example is median filtering which I will talk about a later lecture so linear spatial filtering usually perform a sum of product operation between an image F and a filter kernel which we call here W so

**1:05:19** · the kernel as I said before is an array which defines the neighborhood of the operation and its coefficients and define the nature of the filter so a kernel is usually also called a mask or a template or a window so here you can see an example of a 3 by 3 kernel for

**1:05:40** · each location we have a weight and also we have a coordinate coordinate which are defined based on the center of the kernel so if at the center we have W of 0 0 top-left corner will be the value of negative 1 and negative 1 and bottom right corner will be W of 1 and 1 so now

**1:06:05** · let's just say we want to find the response of the image at any given location to the filter or to the kernel so this is computed by the sum of product of the kernel coefficient and the image pixel income passed by the kernel so if we have this kernel and we

**1:06:28** · put the center of this kernel at location x and y there response of the image to this kernel for that location which we denoted here by G of X and Y is going to be W negative 1 negative 1 multiplied by f of X minus 1 y -1 plus w na one zero multiplied by f of X minus 1 W sorry y and then all the way to W 1 + 1

**1:06:57** · multiplied by f of X plus 1 and y plus 1 as we change the coordinates of x and y the center of the kernel moves from pixel to pixel and generate the final filtered image so as I said the center coefficient of the kernel the value of 0 0 always aligned with the pixel at the location x and y so we can make a more

**1:07:29** · general form of this as I said before it's very common to use kernel sizes for which both the number of rows and the number of columns or odd numbers so if

**1:07:45** · we have that for a kernel size of M by n lowercase M multiplied by lower case and any both of these values are odd we can define m to be 2a plus 1 for which a is a non-negative integer and we can define n to be a to be plus 1 again B Eve and non-negative integer so if we have that we can reformulate the previous equation into this very nice form in which G of X

**1:08:18** · Y is the summation over s changing from negative a to a and summation for T changing from negative B to B of W of s NT f of X plus s and y plus T so for the

**1:08:37** · previous example we had MN n to be both 3 so if we have that the value of a is going to be 1 the value of B is going to 1 and if we replace a and B as 1 in this equation then we get to have this the

**1:08:56** · same equation of course when we have kernels of larger sizes its much better to write the filtering operation in this form because it's much more concise and I as I said before we

**1:09:12** · change the values of x and y basically we move the kernel from pixel to pixel across the image and for each one of them we compute the response of that a small neighborhood to the kernel and based on those we can create the full filtered image so the definition that I

### Correlation vs. Convolution

**1:09:36** · just gave you in the previous slide is the definition our correlation between two functions so I repeated and that definition here but only for a one-dimensional function so in the book

**1:09:56** · the correlation is shown by an empty store but there is another common a symbol for showing the correlation which is a circle plus sign so in the previous equation if we assume that we are only having one variable then it is going to be simplified to this equation but in

**1:10:20** · addition to correlation we have another concept called convolution which is usually showed by a black store or a circled multiplication sign in which as you can see instead of finding the multiplication between WS and f of X plus 1 here we do the multiplication up W with f of X minus s so you might say

**1:10:51** · okay so by itself and the change is not that significant so let's look at an example to see how this is slightly different formulation can produce some different properties so to do that lets just assume a kernel simple one-dimensional kernel one two four to an eight and let's just apply this kernel to a function f that looks like

**1:11:24** · zero zero zero one zero zero zero zero so this function is usually called a discrete unit impulse and it's definition in the discrete domain is like this so Delta X minus zero is zero everywhere except their x equals x zero

**1:11:46** · so for example here if we assume the origin to be here and like we show this as location zero then this function function f is actually Delta of X minus three because at location 3 its value is 1 and everywhere else its value is zero so now let's just find the correlation between this function and this kernel so

**1:12:16** · first of all for the kernel we have its center to be the the middle pixel here so the center is four so first we put this kernel at the first location so basically we align the center pixel at the first location of the function but one thing that you might notice is that the value 1 and the value 2 basically fall outside the boundary of function f so to avoid having undefined values we

**1:12:50** · usually zero extend the original function by some zeros either to the left or to the right so since here we have two values that

**1:13:06** · fall outside we just put two zeros to the left so now we don't have any undefined values after doing this what we do is that we find the element wise multiplication between the kernel and the function and we sum them all together so 1 x 0 plus 2 x

**1:13:29** · plus four x zero all the way to 8 x zero and as you can imagine the value will be zero so this is the value first value that we get then we move this kernel one

**1:13:47** · step to the right and now we are going to be in this position so now if we find the element wise multiplication and sum them all up together we have eight x one plus two x zero all the way to 1 multiplied by zero so the result of this is going to be 8 so this is the second element we do it for the third element of force element all the way to the last element of the original function f so if

**1:14:19** · we do that this is the correlation result that we get so one thing that you notice is that the kernel basically the correlation result is the reverse kernel at location for which F is 1 so now

**1:14:40** · let's see what happens for the convolution the effect of having this formulation is similar to basically pre rotating the kernel 180 degrees and then applying the same correlation procedure so for convolution we pre rotate this 180 degrees so instead of having 1 - 4 - 8 now we have 8 - 4 to 1 then place it

**1:15:10** · place its center at the first location again since we have two values which fall outside the boundaries of F we add two zeros basically we zero path the original image and then we again find the element wise multiplication and then

**1:15:30** · sum the result so for the first one the result is going to be 0 if we move this one step to the right now we have the result of one and then two and then four and then two and then eight so one thing that you might notice is that when we pre rotate the original kernel now for the result of convolution we basically have an original replica of the kernel at the

**1:16:01** · location where the original image has a value of 1 or basically the discrete unit impulse had the value of 1 and that is something that is very useful in practice so again pre rotating the kernel revolved in an exact copy of the kernel so in effect we can say linear spatial filtering and spatial convolution or synonymous but

**1:16:29** · this was only for a one-dimensional case let's just see what happens for a 2-dimensional case for the two-dimensional case this is the exact same definition that we had in a previous slide so we have the summations from negative a to a and negative B to B over the two variables of the function

**1:16:56** · for the convolution we have the variables of summation to be basically inverted or like with negative sign so let's see what is the effect in both correlation and convolution so since we are working with two-dimensional functions now the original image it all zeros with one at the center and the kernel that we have a 3 by 3 kernel with

**1:17:27** · values 1 all the way to 9 again since we want to avoid have any undefined value V 0 pad this data so in the previous case what we did was we 0 padded along the only one axis that we had it was a 1 dimensional signal but now since the two dimensional will be row padded both along the horizontal and vertical direction for the correlation again we

**1:18:01** · place the center of the kernel at the first pixel of the image right basically this is the first pixel of the image and this is basically after zero padding

**1:18:16** · right so what we do is that we find the element wise multiplication between the element of the kernel and pixel values of the original image and then we sum them together so if we do this for this location first they get the value of 0 which is here if we move with one pixel to the right again we get 0 one pixel to

**1:18:41** · the right zero and then all the way until the last element of the first row then we move this one pixel to the light well one pixel down and then we do the same so after repeating this process for all the pixels in the original image this is the correlation result that we get and as you can see in comparison to the original kernel this eve reverse in both horizontal and vertical direction

**1:19:12** · so now for the convolution what we do is that we basically flip the original kernel in both horizontal and vertical direction and repeat the correlation process so this is a view of the rotated

**1:19:30** · or like flipped kernel in both horizontal and vertical directions and after doing the correlation of the image with this kernel this is the result that we get and as you can see basically we have exactly the same kernel at the location for which the value of function f is 1 so again pre rotating the kernel

**1:19:59** · result in an exact copy of the kernel and again for 2d cases linear spatial filtering and spatial convolution are considered to be synonymous so even though you might say

**1:20:15** · the difference between correlation and convolution is not that significant and it's only you'd basically get the exact same result if you flip the kernel along both horizontal and vertical direction but when you talk about more advanced

**1:20:37** · filtering procedures that are done in image processing going with convolution instead of correlation has a lot of benefit to go over the list just see what are the properties of convolution and correlation so for the first property for convolution we have the commutative property which basically means that convolution of F and G is equal to the convolution of gnf but we

**1:21:11** · cannot say the same thing for correlation so correlation of F and G is not the same as correlation of gnf so because of this nice property of the convolution it doesn't matter whether we

**1:21:29** · pre-rotate the kernel or the image we always get the same result but for the correlation it's different if we find the correlation between the image and the kernel or from the kernel and the image there is another property with

**1:21:47** · which is called the associative property which basically says and that the correlation of and the convolution of F and the result of convolution of G and H is equals to the convolution of F and G convolved with the function h so as you

**1:22:09** · can see basically it doesn't matter where better we first find the convolution of F and G and then convert the result with it or if we calculate the convolution of G and H first and then convolve the result with F but again we cannot say the same thing about the correlation and finally we have the

**1:22:33** · distributive property which is common in both correlation and convolution which basically says that we can distribute the convolution and correlation over a summation so because of the commutative property of convolution as I said it is not important whether the kernel or they may be is pre rotated also and this is a very useful feature is that when we have multiple stages of filtering it is very

**1:23:05** · useful to use this commutative and associative properties because what we can do is that we can first convolve all the filter kernels first and then convolve the result with their with the image so it in terms of final result it doesn't make any difference but we cannot say the same thing about correlation so the takeaway message is

**1:23:36** · that spatial filtering is always done using convolution instead of correlation of course there are some cases that you can interchange these especially for deep learning applications but that is a topic that probably will be covered by the end of the course so now let's talk

### Separable Kernel Filters

**1:24:02** · about separable no filter kernels if you remember when I was talking about converting an image to a transform domain for example going from a spatial domain to frequency domain I talked a little bit about separable kernels so generally speaking a 2d function G of XY is set to be separable if it can be written as the product of two 1d functions so G of X multiplied by G 1 of

**1:24:34** · X multiplied by G 2 of Y so for example let's just say we have this kernel we say that it is separable because we can write it at the form of multiplication of C and R right so we multiply C in its

**1:24:54** · original form with the transpose of R and if we do that we get exactly the same kernel so if you have a separable kernel size of lowercase M by lowercase n we can express it as the outer product of two vectors V and W so in which we have M rows and one column and W has n

**1:25:26** · rows and one column if the kernel is square basically has same number of rows and column in that case it can be even simplified to only needing to know one

**1:25:48** · kernel basically one of the kernels and then if we multiply the kernel with its transpose we get to there we get their original separable kernel kernel so this outer product that we define here is basically equivalent to the 2d convolution of a column vector and a row vector so now let's see how this equivalency is beneficial to us so do

**1:26:18** · you remember we said that the convolution has some nice properties we had a commutative property basically we can inter change the location of the function when we perform convolution and then we had the associated property which basically said that is the order of the convolution is not important when you have more than one convolution so

**1:26:44** · now if you have that let's just say we have a separable kernel called W and we want to find a cat convolution between W and F so now since W is separable and since we said that

**1:27:00** · the outer product let me define here so whether the kernel is rectangular kernel or like a the square kernel it doesn't matter if outer product is equivalent to convolution so now that means that we can write W in terms of w1 convolved with w2 so if we use the commutative and associative properties we can see that W

**1:27:29** · convolved with F equals w1 convolved with F and the result of this calculation is composed with Derril e2 so now why is this important it is important because it means that if we have a separable kernel we can basically

**1:27:49** · reduce the number of calculations that we need to do in order to find a filtered result so generally speaking the computational advantage of a separable kernel in comparison to an insuperable separable kernel in terms of the number of multiplications and summations I can be drived I have this ratio so if the colonel is non-separable we have to have M by n by M by n number

**1:28:23** · of calculation multiplication than addition but if it's a parable this number is reduced significantly so the ratio between the two is basically gives us the amount of

**1:28:41** · advantage that we get if we perform the convolution in a separable way so for example if our kernel of size 11 by 11 just this simple change gives us five point five times boost in terms of computational performance it's even higher for the kernels of larger size so for example if our kernel is 101 by 101 it gives us

**1:29:12** · more than 50 x advantage so now that we learn this let us see how we can create a separable kernel based on a kernel so

**1:29:29** · to do that first we need to verify if the kernel is separable to begin with so usually the matrices that are formed by a product or the column vector and a row vector always have a rank of 1 so in another word rows and columns of such matrices are linearly independent meaning that the rows only differ by a constant multiplier and again columns are only different by a constant multiplier but how can we if you are

**1:30:03** · given a kernel how can we see if the rank is 1 or not so the mathematical derivation of the equation is out of the scope of this course for us since we only care about the rank and not necessarily how this rank is calculated I suggest you take a

**1:30:27** · look at the rank function in MATLAB so you will give a matrix to this function and it provides the rank of there the matrix so if you are given a matrix or a kernel that you know that you want to see if you can represent it as a separable set of kernels first you use

**1:30:54** · the rank function to determine if the rank is 1 or not if the rank is 1 then you follow this three-step process to basically come up with the separable kernels first you find any nonzero element in the matrix and you denote its value as e so this can be any non

**1:31:19** · an element in the matrix not necessarily the first one or the last one after you select that nonzero element then you form two vectors C N or equal to the column and row in the kernel that contained that exact element so after

**1:31:40** · doing that then you can define the two separable kernels and V and W transpose as V being equal to the column vector that contains element E and there will be transport the row vector divided by E

**1:31:59** · basically the row vector that contains Y divided by E and just by doing this simple transformation for any kernel that has a rank of 1 you can come up with two separable one dimensional kernels which you can convert with your image in any order you want and over all the computational complexity is going to

**1:32:29** · be much less than if you basically convolve the original kernel with that image since in the next lecture I'm gonna talk more about different spatial filtering and that we can have and a lot

**1:32:46** · of the concept can be better represented in the frequency domain let's just briefly go over some of the useful property frequency domain of course more consideration and more discussion of the properties will be done in chapter 4 of

**1:33:03** · the book so as you know Fourier transform is used to go from the spatial domain to frequency domain so in effect free transform the compose of the signal or here the image into each frequency component so there are

**1:33:23** · two fundamental properties that you need to consider first of all if the in terms of the convolution so convolution in the spatial domain is equivalent to element wise multiplication in the frequency domain and vice versa so that

**1:33:43** · means that if you want to find the response of an image to a kernel in the spatial domain you have to find the convolution between the image and the kernel but in the frequency domain what

**1:34:00** · you need to do is that first find the frequency or free transform of the kernel and the image and then in the frequency domain you just simply calculate the element wise multiplication and the same goes for other way too so if you have a convolution in the frequency domain that is equivalent to multiplication in their spatial domain and the second fundamental property is that if we have

**1:34:29** · an impulse function of amplitude a in their spatial domain it is going to be a constant function of value a in the frequency domain and vice versa so here you can see an example of a filter that

**1:34:48** · is defined in the frequency domain so considering you as the frequency and the vertical line as the amplitude in any frequency in this region whatever frequency we have in this region will get a value of 1 that means that it will be passed to the final result but anywhere here will be stopped because the amplitude is going to be 0 and its spatial equivalent looks like this of

**1:35:22** · course this is beyond what I want to cover in this lecture we will see more specific when we talk about frequency transform or Fourier transform but it is useful to know how we usually build a spatial filter so there are three main approaches for building a spatial filters one is by formulating based on mathematical properties so for example we can use integration or averaging for blurring an

**1:35:55** · image or we can design a special filters which compute the local derivatives to sharpen or enhance the edges of an image the other way is by sampling A to D special function for which the shape has a desired property so for example we can

**1:36:16** · create a weighted weighted average filter by sampling A to D Gaussian function or we can sample the inverse Fourier transform of A to D filter that is specified in the frequency domain and finally we can design a special filter with a specified frequency response for

**1:36:36** · example designing a one-day spatial filter and then forming a separable or like circularly symmetric 2d version of that of course we will see more examples of these in the upcoming lecture so in

**1:36:51** · the next lecture I will talk about smoothing lopes and spatial filters sharpening hypothesis special filters then high-pass band reject and bandpass filters designed based on the low-pass filters and finally how we can combine a spatial different spatial enhancement method that we talked so far to improve the appearance of images