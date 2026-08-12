---
title: "Digital Image Processing - Part 12 - Introduction to Image Compression and Watermarking"
source: "https://www.youtube.com/watch?v=WamFr2gQgyk&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=12"
author:
  - "[[ASIP-Lab]]"
published: 2020-08-24
created: 2026-08-12
description: "Topics:00:47 Image Compression Fundamentals11:18 Redundancies16:11 Measuring Image Information21:14 Fidelity Criteria24:52 Image Compression Models32:28 Image Coding34:50 Image Watermarking"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WamFr2gQgyk)

Topics:  
00:47 Image Compression Fundamentals  
11:18 Redundancies  
16:11 Measuring Image Information  
21:14 Fidelity Criteria  
24:52 Image Compression Models  
32:28 Image Coding  
34:50 Image Watermarking

## Transcript

**0:00** · welcome to the twelfth lecture of the digital image processing course in this lecture I will give you a brief introduction to image compression and watermarking so the topic that will be covered in this lecture or image compression from the mentals definitions of different types of redundancy is that we can have an image data how we can measure the amount of information in an image then I will talk about the

**0:32** · fidelity criteria that is commonly used for comparing the result of image compression to the original images finally a brief overview of the image compression models image coding and watermarking so let's just begin with the fundamentals so data compression is the process of reducing the amount of data that is required to present a certain amount of information so based

### Image Compression Fundamentals

**1:01** · on this definition you can easily see that the data and information are not the same in this contact data is serving as means for conveying information so because of that you can have various amount of data to represent the exact same amount of information so since we

**1:24** · have this we may end up having redundancy if irrelevant or repeated data is being used to convey a certain amount of information so to quantify the amount of redundancy let's just take a look at some definitions so assuming B and B prime as the number

**1:47** · of bits that are used for representing the same amount of information using two different techniques so the relative data redundancy here we call it or with B bits it calculated using this simple equation R equals 1 minus 1 over C and in this equation C is known as the compression ratio which is the ratio between B and B Prime

**2:18** · so an image processing B is the total number of bits that is used to represent an array of intensity values so let's say if you're working with a 100 by 100 pixel image and each in each pixel is represented by 8 bits so in total B becomes 100 multiplied by 100 multiplied by eight or eighty thousand bits so as I

**2:47** · said depending on the system that we use for compressing or representing the information we may end up having redundancies so there are three types of redundancies common in images we can have coding redundancy which is caused by more than necessary bits in the code word that are used for representing images so let's say if you have an array

**3:14** · of values to the array of values for which the range of the values can change between 0 and 255 so in this case if you have all the possible intensity values only having 8 bits to represent the intensity information is enough but if you use code words that are 16 bits you

**3:41** · are using more than necessary bits to represent the image so that is an example of coding redundancy we can have a spatial and temporal redundancy which is caused by the correlations between pixels of an image or a sequence of images cause that causes unnecessary duplication of information so let's say you are working with a video in which

**4:06** · most of the objects in the scene or our fix and not moving so this is an example of having temporal redundancy so if you want to store this data you only need one copy of the object that are not moving so that can help you

**4:27** · reduce the amount of redundancy in your data and then finally we can have irrelevant information which is information that is irrelevant to the feature of our interest so here you can see three different examples each containing one of these redundancies we have this one which has coding

**4:51** · redundancy we have we have this one which had spatial dependency and finally we have this image which you can say contains irrelevant information so let's just go into more detail and see how these images contain these different types of redundancy so before we do that

**5:13** · let's just go over some definitions for coding redundancy so we start by the definition of the normalized histogram so by by this point you have seen this definition many many times so I assume a random variable or K in the interval 0 and L minus 1 is used to represent the intensity levels of an m-by-n image so based on this the normalized histogram can be shown using this equation PR of

**5:43** · RK equals and K over m multiplied by n in which case I can change between 0 and L minus 1 so here PR is the probability of intensity value or K and K is the

**6:00** · number of times that this intensity value or K appears in the image and the denominator is M by n which is the total number of pixels in that image so now let's just say we use a separate function L of RK to represent the number of bits that is used for representing each value of RK so based on this new

**6:25** · function the average number of bits that is required to represent each pixel in the image can be calculated using this equation so we have capital l average the average number of bits over the entire image equals the summation of l RK x PR k basically the number of bits

**6:50** · per pixel multiplied by the probability so number of bits per intensity level and multiplied by the probability of that intensity level and this summation is calculated for values of k changing from 0 to L minus 1 so up until now what we had before was L of RK to be a fixed value so we were working with an 8 bit image L of or K is a constant 8 but this

**7:20** · is not necessarily the case always so you can have different coding techniques that use variable length for representing different intensity values so now let's take a look at one example and see how this calculation can show

**7:43** · the amount of redundancy that we can have in an image especially specifcally coding redundancy so the image on the left you can see is 256 by 256 8 bit grayscale image but if you look closely you see that there are only four different intensity values that are present in this image so we have 87 we have 128 we have 186 and we have 255 so out of the tube 256 possible intensity

**8:18** · level that you can show with 8 bits only four of them are present here if we calculate the normalized histogram these are the probabilities of each one of these intensity levels in the image so now let's just compare two cases one if we use an a fixed length code

**8:41** · with length eight here we call it code one and as you can see we can have different representation of the intensity value so clearly this is not wrong this is only four for example but each one of the intensity value is shown with an 8-bit code and here as you can

**9:04** · see the number of bits per intensity level is eight bits the second case is if you are using a variable length code so here as you can see for representing intensity level 8787 we use code zero one four one twenty eight we use one for 186 we use three and for 255 we also use a three

**9:33** · bits to represent this intensity level and based on this we have l2 to be two one three and three so now if we use the equation for L average we see that for code one the average number of bits that

**9:53** · is required that is used for representing this image is eight bits while for the second code the average number of bits is one point eighty one so now based on this if we want to calculate the compression ratio and the relative data redundancy that we have between these two representations we can simply use the equation for for C which

**10:21** · was the total number of bits for one representation divided by the total number of bits for the other representation so usually it is the largest number of bits is an on the

**10:36** · numerator and the smallest one is on the denominator so for code one it's going to be M by N by eight and four code - it's going to be M by n by 1 point 8 1 so if we do this calculation this is approximately 4.4 to and based on this if we calculate the relative data redundancy we have the

**11:01** · relative data redundancy to be zero point seven seven four which means that seventy seven point four percent of the data in the original 8-bit representation is redundant so now let's

### Redundancies

**11:20** · take a look at another example to see how a spatial and temporal redundancy is work so on the Left we have a 256 by 256 image and we are using eight bits to represent all the intensity values if we draw the histogram of there's a specific image we see that all the intensity values have exactly the same probabilities so since all the 22:56

**11:51** · intensity levels have identical probabilities to represent and preserve all the information in the image we need to have eight bits to represent all the intensity values however we see that all the pixels in the same row of the image have identical intensity values and that is an example of spatial redundancy so a

**12:15** · better way to represent such image is by using a sequence of run length pairs in which you specify the start of a new intensity value paired with the number of consecutive pixels that have that intensity value so if you do this this image 256 by 256 can be only represented by a 256 by 2 matrix

**12:47** · so here this can be done by replacing each row with a single 8-bit intensity value and the length of 256 add the length of the row so this this way you can see how you can compress the information that is in this image in

**13:06** · such a way that you end up with much less number of bits to be used for the representation of that information what about irrelevant information so the image on the left is mostly gray right

**13:26** · so and just by looking at this image you don't see any variations in the intensity but if we create a normalized histogram for this image we realized that we actually have some variations in the intensity even though all of them are happening almost in the middle of

**13:51** · the intensity ranges so to see what other information are present in this image we can do one of the techniques that we have design before for improving the histogram so if we apply histogram Equalization on this image this is the the result of the histogram equalization so the original image appeared as a homogeneous field of gray to the human

**14:24** · visual system that can be represented even by a single 8-bit value so you can just say I have an image of this size and the intensity values for all the pixels is let's say 125 on the other hand the histogram equalized variance shows some patterns that are not visible in the original image so now the question becomes our ordeal additional

**14:49** · information that you see in the histogram equalized image or irrelevant information or because if they are irrelevant information and you can represent this image by the average of all of it intensity values then you can heavily reduce their the amount of data that you

**15:11** · use for representing this image but if you say no these very fine patterns are also important in that case you cannot have any sort of compression and you need to represent all the intensity values so whether the image can be represented by a single value or as a whole without any compression depends on their specific application for example if you are working with medical images

**15:37** · usually you need to preserve all the information that you have so you cannot afford to lose any information but for let's say for representation purposes for visualization purposes if you only want to visualize this you can see that you can only use one intensity value one value to represent this this whole image so depending on the application you need

**16:05** · you can consider some of the information to be relevant or relevant so now that we have talked about these how can we measure the amount of information in an image the answer is in the concept from

### Measuring Image Information

**16:22** · information theory so if you have a random event here we call it E that has a probability of happening here we call it P of Y we say that this random event contains I of a units of information so

**16:39** · how is this calculated simply by calculating this equation of course the main idea behind deriving this equation is not going to be covered in this course so if you are interested you can refer to more relevant courses on information theory so I have e equals log of one over the

**17:03** · probability of e or minus log of probability of e so what do we get from this equation so if P of E is 1 which means that the probability of this event happening is 100% then the amount of

**17:24** · information contained in this random event is zero based on this equation so that means that the less probable is an event the more amount of information you can have or in another word the more

**17:43** · random an event is the more information that it has so now let's just assume we have a sequence of independent random events here we call them a1 to AJ and each one of them has its own probability of happening P a1 P a2 all the way to P AJ so now based on this we can define what is called to be entropy of the

**18:10** · sources of these random event and it is defined as H equals negative summation of P AJ multiplied by log of P AJ and this summation is calculated for J changing from 1 to J so the entropy you

**18:29** · can say it is equivalent to the amount of information for these series of events so if you are working with an image with intensity levels RK and probabilities P R / K and since we are working with binary values this log is changed to log 2 we can calculate the

**18:54** · entropy of the the image or equivalently the amount of information in that image by this equation so H tilde equals negative the summation over K changing from 0 to L minus 1 basically over the thought number of intensity values PRK their probability of each intensity value multiplied by log to our PRK which in

**19:22** · essence is the lower bound on the compression that can be achieved when coding statistically independent pixels directly so what do we mean by that the meaning is that we assume that all the pixels are independent of each other this is not necessarily the case for the image data but it is a good enough estimate that we can use for our

**19:50** · calculations when we want to compress images so now let's see what is the amount of in entropy in the image that we have seen before for these three images if we calculate the entropies for the first one the entropy is one point six six four for the second one the entropy is eight and for the last one the entropy is one point five six six bits per pixel respectively so again

**20:24** · remember that the entropy is a lower bound on the compression that can be achieved when coding statistically independent pixels directly so in the images this is not usually the case why because we can we can have spatial and

**20:43** · temporal correlations between the pixels as well right and the general definition for entropy is not considering though the spatial and temporal correlations that we have between a pixel but in any case the amount of entropy and the information in an image they are correlating with each other even though this correlation may not be intuitive

### Fidelity Criteria

**21:14** · so now let's just quickly go over their fidelity criteria that we usually use for comparing the performance of image compression algorithms so compression may cause loss of information so there are generally two types of criteria that can be used for assessing the performance of compression algorithms we can have objective metrics in which we

**21:42** · have a mathematical expression that shows the amount of error between the original image and it compressed version so for example we can use root mean squared error the first equation or we can use min squared signal-to-noise ratio the second equation so as you can see the derivation of these equation is pretty straightforward for the erm s we calculate the difference between the compressed image and the original image for each pixel we take it to the power

**22:16** · to calculate the summation and we take the average and we calculate the square root of this value as for the signal-to-noise ratio the denominator is a good estimate of the noise or the difference between the original image and compressed version and in the numerator we have basically there the

**22:42** · power of the of the image so we are calculating the the ratio between the power of the image and the power of difference or noise the other type of metric that we can use is the class of subjective matrix in which humans basically just judge their performance of different compression algorithms

**23:12** · so now let's take a look at one example so here on the Left we have the original image without any compression and then we have the result of three compression image compression algorithm and we want to compare the performance so we can

**23:30** · calculate the root mean square error or RMS error and if we do that the first result has an RMS of five point seven seventeen the second has an RMS of fifteen point sixty seven and finally we have the last one which has an RMS of fourteen point point 17 of course using

**23:55** · RMS by itself is not not enough and if we for example compare these results subjectively you see that the last one is probably the less truthful to the original image because there are several sections of the image that are completely eliminated even though the RMS is less than there the second one so

**24:22** · for subjective compression you can usually devise a table such as the following example and ask human observers to compare the result of different compression algorithm so this table is an example of a rating scale that is used to quantify the quality of

**24:46** · pictures that appear on on TV for example so now let's quickly go over image compression models so an image compression system usually consists of two main components we have an encoder component and a decoder component the encoder component performs compression and the decoder component performs decompression so a codec is a device or

### Image Compression Models

**25:16** · program that is capable of both encoding and decoding also you probably have heard about this a compression system can be either lossless or information preserving or it can be lossy so and you

**25:34** · can see from this image each one of these components the encoder or decoder have some component between them so the input to the system is the image f of X Y or it can be a sequence of images like a movie which is shown by three variables f of X Y and T and the output is f F had X Y or have had X Y and T so

**26:03** · the result of the encoder will be the compressed data that is used for storage and transmission so now let's take a better look at the individual component that we have in this system so at the beginning we have the mapper which transforms the input data into a usually non visual format that is designed to reduce spatial and temporal redundancy so this operation is generally reversible then we have the

**26:34** · quantizer which reduces the accuracy of the mappers output in accordance with some pre-established fidelity criterion for example with less amount of RMS error or with less amount of signal-to-noise ratio and this is to keep irrelevant information out of the compression compressed representation so this operation is lossy and generally it is non reversible so if you plan to have

**27:06** · error free compression you should remove this this step so so far we have seen the mapper which is generally used for reducing spatial and temporal redundancy then we saw quantizer which is generally used to reduce relevant information in

**27:27** · the compression results and then finally we have symbol symbol encoder which generates a fixed or a variable length code to represent the quantizer output and this operation is is reversible so

**27:43** · mapper is for reducing spatial temporal redundancy quantizer is for reducing relevant information and symbol encoder is generally for reducing coding redundancy so now in the decoder part we

**27:59** · have the symbol decoder and the inverse mapper that perform the inverse operation of the encoder symbol encoder and mapper respectively so they can see since the quantizer is generally not reversible we don't have any equivalent component in there in the decoder so

**28:23** · when we talk about images there are some definitions that we need to consider we have the definition of image forward which is a standard way to organize and store image data we can have image container which is similar to a an image format but usually handles multiple types of image data and finally we can have image compression standard which defines all the procedures for compressing and decompressing images and

**28:54** · basically reducing the amount of redundancy that we have in the original images so here you see a general chart of different image formats that are currently used so we have two cases one

**29:13** · for still images one for videos or sequences of images as for still images we can even either have binary image zero and one like an white image or we can have a continuous tone or grayscale image as you can see some of these techniques are colored in blue while some of them are colored in black so the blue ones are the format's and containers that are internationally sanctioned while the one in black they

**29:44** · are not in internationally sanctioned but still they are widely widely used so here you see the previous chart in much more detail we have different standard internationally sanctioned standard four by level or binary images we have JPEG

**30:11** · for example which is probably the most well known technique out of these which is short for joint photographic experts group standard which uses discrete cosine transform and as one of the main building blocks for doing the compression there are more advanced versions of it as well so JPEG by itself is lossy but we have jpeg-ls which is

**30:37** · the lossless to near lossless standard basically improves the performance of JPEG and finally we have cheap JPEG 2000 which is again a follow-up on the JPEG standard for increased compression JPEG

**30:56** · images it uses different coding algorithms and also it uses discrete wavelet transform instead of discrete cosine transform that was used in original JPEG and for the

**31:12** · internationally sanctioned with your compression standard you have probably seen some of these so we have mpeg-4 we have h.263 and all of these if you are interested you can refer to the

**31:31** · corresponding sections in the in the book for example Divi is mentioned in section eight point nine or mpeg-4 is mentioned in section eight point eight so if you're interested you can follow up on that by referring to the book or any other material that covers these type of techniques and finally we have a more detailed version of the chart for

**31:59** · popular image and video compression standards so these are not necessarily internationally sanctioned but and you probably can detect from their name they are widely popular we can have BMP we can have gif which is short for graphic interchange format we can have PDF PNG gif F web P and we have some techniques for video compare compression so there

### Image Coding

**32:30** · are some common image coding method that are widely popular and they are covered in the book I'm not going to go over them individually because this lecture was only for a brief introduction to the basic concepts of image compression so we can have Huffman coding which is a version of variable length coding we have can have more advanced version coulomb and arithmetic coding lvw coding

**33:03** · we can have wrong length coding you have seen one example at the beginning that we can use the distorting position of an intensity level and dead the duration or

**33:20** · the number of pixels that that intensity level is repeated so that is a basic example of run and coding as for the symbol based coding you can think of it the technique that is used for compressing binary images mainly scan text document

**33:46** · we can have bit plain coding if you remember from the first few lectures we said that we can divide our images into different bit planes based on the the weight of the binary weight of each one of these bits in the image so that is one possibility that you can use to compress your images we can have block transform coding in which we divide our

**34:19** · image into smaller blots and we use some sort of discrete Fourier transform discrete cosine transform or discrete wavelet transform to find the appropriate coefficients and use those for quantization and reducing their redundancy and we can have predictive coding and more advanced wavelet coding for compressing video files as well so

### Image Watermarking

**34:51** · now that we have seen different image compression algorithm at least we had a better idea about general concept behind image compression it's only natural to talk about image watermarking too so image watermarking is the process of inserting data into an image and this is

**35:14** · a common technique that is used for copyright identification user identification authenticity determination automated monitoring and copy protection so in general we can have two different types of watermarks they can be either visible in which we have an opaque or semi-transparent sub image that is placed on top of another image or they can be invisible in which

**35:41** · the watermark cannot be seen by the naked eye but if you have appropriate decoding algorithm you can recover or extract the warmer there is an and there is another way of classifying different watermarking techniques they can either be fragile in

**36:02** · which the watermark is destroyed when the image is modified or they can be robust in which watermarks or survives image modification so let's just take a look at two very basic techniques for image watermarking so the first one is \[Music\] the very basic image watermarking that is achieved by applying this equation so

**36:34** · we have F of F W which is the watermark image we have F which is the original image and finally we have W which is the watermark image and what you can do is that you basically calculate a weighted summation of the original image and watermark so how are these weights are determined by this parameter alpha so

**36:59** · alpha is a constant that controls the relative visibility of the watermark and the underlying image as you can see we have 1 minus alpha multiplied by F and alpha multiplied by devil you so alpha has a is a value is a constant value between 0 and 1 so if alpha is 1 that

**37:23** · means that FW is only going to be watermark if alpha is 0 that means FW is going to be only F anything in between we have different ratios of F and W combined to create after value so let's just say we want to add this watermark into the Lehner's image for starters you

**37:46** · should know that 2 for this arithmetic calculation to be valid you need to have both F and W having exactly the same size so if your watermark is smaller than the original image you need to add basically you need to zero pet it but in any case after that is done this is the the watermark image and if

**38:09** · you calculate the difference between this image and the original image you can have a good estimate of the the watermark watermark is itself so that is one example of simple image watermarking and this as you can see results in a visible watermark so now let's take a look at another example here we have an example of an invisible

**38:39** · fragile watermark that is generated by the following equation so we have fw x equals 4 x f / 4 + w / 64 so the first

**38:56** · time that you look at this equation you might think that okay why do we divide F by 4 only to multiply it by 4 what difference does it make so one thing that you should notice is that these multiplication that division are all done using unsigned integer arithmetic so that means that we if let's say we divide an intensity value 10 divided by 4 we don't get 2.5 since we are working

**39:27** · with integer arithmetic we get 2 right so dividing and multiplying by 0 sets the two least significant bits of f 2 0 dividing W by 64 shift its two most significant bits into the two least significant bits position so now if you add these two together you generate what is called to be the least significant bit or LSB watermark image so this one

**40:01** · this original image and this is the watermark that we want to apply so this is the result so even though you don't see there the watermark image but you should realize that just by applying this simple equation you using unsigned integer arithmetic what

**40:23** · we what we have done is that we basically eliminated the least two significant bits of the original image and we replaced those two significant least significant bits with the watermark image so this is basically what you see here this is the watermark image even though you are not able to see there the the watermark itself but

**40:50** · why do we say this is an example of a fragile watermark the reason for that is that if you apply JPEG compression on this image and then try to extract the watermark this is basically what you get why because JPEG compression and eliminate some of the unnecessarily

**41:13** · unnecessary information in there in the image of course there is no way for the for the JPEG compression to know that we have added a watermark and invisible watermark to the to the image so because there is no distinction in JPEG compression it basically eliminates those information associated with the watermark has none necessary information

**41:43** · so these were only two basic techniques if you are more interested on the other technique more robust techniques for watermarking feel free to look online and refer to appropriate documents and

**42:02** · papers that discuss these techniques so by this I conclude the last lecture of the digital image processing course so during this course we have learned so much we started with basic intensity transformations and then we move to different techniques for spatial filtering we extensively talked about

**42:28** · fast Fourier transform how it's calculated for for discrete or digital images what are those properties and how we can apply filters in the four-year domain then we move to image restoration we talked about noise reduction without about different types of degradation that can happen in the images we discussed

**42:53** · extensively on the topic of edge detection image thresholding and segmentation we talked about color image processing and finally for the last lecture we talked about introduction to image compression and watermarking so from now on you should have a good foundation different areas of image

**43:19** · processing of course we only barely basically scratch the surface so there are definitely more for you to learn but you should have a good foundation to start learning on your own write your own code and experiment with image processing libraries that you see so good luck image processing