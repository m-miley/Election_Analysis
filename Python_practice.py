# print("Hello World!")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")


# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

# for county in counties:
#     print(county)


# for i in range(len(counties)):
#     print(counties[i])

# candidate_votes = int(input("how many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (f"""
#     You received {candidate_votes} number of votes.
#     The total number of votes in the election was {total_votes}. 
#     You received {round((candidate_votes / total_votes * 100), 1)}% of the total votes.
# """)
# print(message_to_candidate)


# candidate_votes = int(input("how many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (f"""
#     You received {candidate_votes:,} number of votes.
#     The total number of votes in the election was {total_votes:,}. 
#     You received {candidate_votes / total_votes * 100:.1f}% of the total votes.
# """)
# print(message_to_candidate)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for dict in voting_data:
    print(f"{dict['county']} county has {dict['registered_voters']:,} registered voters.")
