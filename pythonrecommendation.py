print(" <<-------AI Recommendation System------->> ")

interest = input("Enter your interest (coding, sports, music, movies): ").lower()

if interest == "coding":
    print("\nRecommended:")
    print("- Learn Python")
    print("- Practice on LeetCode")
    print("- Build Mini Projects")

elif interest == "sports":
    print("\nRecommended:")
    print("- Football")
    print("- Cricket")
    print("- Badminton")

elif interest == "music":
    print("\nRecommended:")
    print("- Arijit Singh")
    print("- Taylor Swift")
    print("- Imagine Dragons")

elif interest == "movies":
    print("\nRecommended:")
    print("- Inception")
    print("- Interstellar")
    print("- Avengers")

else:
    print("\nSorry! No recommendations found.")
    