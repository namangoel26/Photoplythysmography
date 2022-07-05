#Some Theory and Background
#The heart rate signal contains a lot of information, not just about your heart but also about your breathing, short-term blood pressure regulation, body temperature regulation and hormonal blood pressure regulation (long term). It has also (though not always consistently) been linked to mental effort, and not surprisingly so since your brain is a very hungry organ, using up to 25% of your total glucose and 20% of your oxygen consumption. If its activity increases your heart needs to work harder to keep it supplied.
#The measures we are interested in can be split into time-series data en frequency domain data. If you are familiar with fourier transforms the frequency part will make sense. If not, the wikipedia page has a good explanantion, and also a very nice visualisation of the process. The basic idea is that you take a signal that repeats over time (such as the heart rate signal), and determine what frequencies make up the signal. You ‘transform the signal from the time domain to the frequency domain’. Here is another visualisation I particularly love, which clearly shows how a repeating signal can be approximated as the sum of different sine waves repeating over time.

# Time Domain Measures – Getting Started
#Looking at the above time-series measures, we need a few ingredients to easily calculate all of them:

#A list of the positions of all R-peaks;
#A list of the intervals between all subsequent R-R pairs (RR1, RR2,.. RR-n);
#A list of the differences between all subsequent intervals between R-R pairs (RRdiff1,… RRdiffn);
#A list of the squared differences between all subsequent differences between R-R pairs.
#We already have the list of all R-peak positions from the detect_peaks() function from the first part, which is contained in dict[‘peaklist’]. We also have a list of R-R pair differences from the calc_RR() function, which is in dict[‘RR_list’]. Great! No additional code written, already 50% of the way there.


#To get the final two ingredients we use dict[‘RR_list’] and calculate both the differences and the squared differences between adjacent values:


RR_diff = []
RR_sqdiff = []
RR_list = measures['RR_list']
cnt = 1 #Use counter to iterate over RR_list

while (cnt < (len(RR_list)-1)): #Keep going as long as there are R-R intervals
    RR_diff.append(abs(RR_list[cnt] - RR_list[cnt+1])) #Calculate absolute difference between successive R-R interval
    RR_sqdiff.append(math.pow(RR_list[cnt] - RR_list[cnt+1], 2)) #Calculate squared difference
    cnt += 1

print(RR_diff, RR_sqdiff)

# Calculating Time Domain Measures
#Now that the ingredients are there, it’s easy to calculate all measures:

ibi = np.mean(RR_list) #Take the mean of RR_list to get the mean Inter Beat Interval
print("IBI:", ibi)

sdnn = np.std(RR_list) #SDNN, the standard deviation of intervals between heartbeats ## Take standard deviation of all R-R intervals
print("SDNN:", sdnn)

sdsd = np.std(RR_diff) #  SDSD, the standard deviation of successive differences between adjacent R-R intervals ## Take standard deviation of the differences between all subsequent R-R intervals
print("SDSD:", sdsd)

rmssd = np.sqrt(np.mean(RR_sqdiff)) #RMSSD, the root mean square of successive differences between adjacent R-R intervals  # Take root of the mean of the list of squared differences
print("RMSSD:", rmssd)

nn20 = [x for x in RR_diff if (x>20)] #First create a list of all values over 20, 50
nn50 = [x for x in RR_diff if (x>50)]
pnn20 = float(len(NN20)) / float(len(RR_diff)) #Calculate the proportion of NN20, NN50 intervals to all intervals
pnn50 = float(len(NN50)) / float(len(RR_diff)) #Note the use of float(), because we don't want Python to think we want an int() and round the proportion to 0 or 1
print("pNN20, pNN50:", pnn20, pnn50)

