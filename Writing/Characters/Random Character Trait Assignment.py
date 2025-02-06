import pandas as pd
import random

filename ="CharacterNames.csv"
names_df = pd.read_csv(filename, sep=",")
names_df["sexual_orientation"] = ""

#print(names_df.shape)
#names_df.head()

def removeElementsFromList(takeOutList, mainList) -> list:
    a = mainList

    # Elements to remove
    remove = takeOutList

    # Remove elements using list comprehension
    a = [x for x in a if x not in remove]

    return a

def selectnFromList (n, listLen, ppl_list = []):
    # number of items
    #n = 10

    # determine which list to sample from
    if ppl_list == []:
        # list of items
        tList = list(range(listLen))
    else:
        tList = ppl_list
    
    # using the sample() method
    UpdatedList = random.sample(tList, n)

    # sort list
    UpdatedList.sort()
    orderedList = UpdatedList

    # remove sampled items from main list
    if ppl_list != []:
        ppl_list = removeElementsFromList(takeOutList=orderedList, mainList=ppl_list)
    else:
        ppl_list = removeElementsFromList(takeOutList=orderedList, mainList=tList)

    
    # return random selections from the list without repetition
    # and the main list 
    return (UpdatedList, ppl_list)

def setSexualOrientation (percentage, orientation, df, ppl_list):

    number_of_ppl = df.shape[0] # number of people one less than it should be for zero index reasons

    n_people_w_orientation = int((number_of_ppl+1) * percentage)

    (index_ppl_w_orientation, ppl_list) = selectnFromList(n= n_people_w_orientation, listLen=number_of_ppl, ppl_list=ppl_list)

    df.iloc[index_ppl_w_orientation,8] = orientation # column 8 is sexual_orientation
    
    return (df, ppl_list)


gay_p = 0.02
lesbian_p = 0.02
gay_lesbian_p = 0.04
bisexual_p = 0.08
pansexual_p = 0.015
asexual_p = 0.015
other_p= 0.01
idk_p = 0.13
heterosexual = 0.71

(names_df, ppl_list) =  setSexualOrientation(gay_lesbian_p,"Gay/Lesbian", df=names_df, ppl_list=[])
(names_df, ppl_list) =  setSexualOrientation(bisexual_p,"Bisexual", df=names_df, ppl_list=ppl_list)
(names_df, ppl_list) =  setSexualOrientation(pansexual_p,"Pansexual", df=names_df, ppl_list=ppl_list)
(names_df, ppl_list) =  setSexualOrientation(asexual_p,"Asexual", df=names_df, ppl_list=ppl_list)
(names_df, ppl_list) =  setSexualOrientation(other_p,"Other", df=names_df, ppl_list=ppl_list)
(names_df, ppl_list) =  setSexualOrientation(idk_p,"idk", df=names_df, ppl_list=ppl_list)

names_df.to_csv('Characters with Orientation.csv', index=False)  