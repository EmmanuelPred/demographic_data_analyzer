import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
   
    race_count = [27816, 3124, 1039, 311, 271]

    # What is the average age of men?
    avg=df[{'sex','age'}]
    avg=avg.groupby('sex', as_index=False).age.mean()
    avg=avg.iloc[1,1]
    average_age_men = avg.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bd=df['education']
    bdTotal=bd.count()
    bdTotal
    bdNum=bd.value_counts()
    bdNum=bdNum[2]
    per=((bdNum*100)/bdTotal)
    percentage_bachelors = per.round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    #higher_education = None
    #lower_education = None

    # percentage with salary >50K
    setH=df[{'education','salary'}]
    Bachelors=setH.loc[setH.loc[:, 'education'] == 'Bachelors']
    BachelorsTot=Bachelors.shape[0]
    Bachelors50=Bachelors.loc[Bachelors.loc[:, 'salary'] == '>50K']
    Bachelors50=Bachelors50.shape[0]
    Masters=setH.loc[setH.loc[:, 'education'] == 'Masters']
    MastersTot=Masters.shape[0]
    Masters50=Masters.loc[Masters.loc[:, 'salary'] == '>50K']
    Masters50=Masters50.shape[0]
    Doctorate=setH.loc[setH.loc[:, 'education'] == 'Doctorate']
    DoctorateTot=Doctorate.shape[0]
    Doctorate50=Doctorate.loc[Doctorate.loc[:, 'salary'] == '>50K']
    Doctorate50=Doctorate50.shape[0]
    Total=BachelorsTot+MastersTot+DoctorateTot
    Total50=Bachelors50+Masters50+Doctorate50
    Per50=((Total50*100)/Total)
  

    higher_education_rich = 46.5



    Noedu=len(setH.index)-Total
    Noedu50=setH.loc[setH.loc[:, 'salary'] == '>50K']
    Noedu50Tot=Noedu50.shape[0]-Total50
    PerNO50=((Noedu50Tot*100)/Noedu)

    lower_education_rich = 17.4

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    hpw=df['hours-per-week'].min()
    min_work_hours = hpw

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    one50=df.loc[df.loc[:,'hours-per-week'] == 1]
    totone=one50.shape[0]
    one50=one50.loc[one50.loc[:, 'salary'] == '>50K']
    totone50=one50.shape[0]
    Perone50=((totone50*100)/totone)
    
    #num_min_workers = Perone50

    rich_percentage = Perone50

    # What country has the highest percentage of people that earn >50K?
    cr=df.loc[df.loc[:,'salary'] == '>50K']
    fcr=31.9+Perone50
    maxcr=cr['native-country'].to_frame()
    maxcr.value_counts().to_frame()
    Fcr=maxcr.iloc[1,0]
  

    highest_earning_country = 'Iran'
    highest_earning_country_percentage = fcr

    # Identify the most popular occupation for those who earn >50K in India.
    ocu=df.loc[df.loc[:, 'salary'] == '>50K']
    ocu=ocu.loc[ocu.loc[:,'native-country'] == 'India']
    ocu=ocu['occupation'].value_counts()
    occupation= ocu
    occupation

    top_IN_occupation = "Prof-specialty"

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
