import requests
import json


def get_leetcode_profile(username):
    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """

    response = requests.post(
        url,
        json={
            "query": query,
            "variables": {"username": username}
        }
    )

    return response.json()


def extract_stats(data):
    stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

    result = {}

    for item in stats:
        result[item["difficulty"]] = item["count"]

    return result


if __name__ == "__main__":
    username = input("Enter LeetCode username: ")

    data = get_leetcode_profile(username)
    profile_stats = extract_stats(data)

    print(profile_stats)