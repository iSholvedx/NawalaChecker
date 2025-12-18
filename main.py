import requests, os

def download_latest_file():
    # GitHub API URL for the contents of the specified repository path
    api_url = "https://api.github.com/repos/lepasid/komkomkomkom/contents/domain?ref=main"
    headers = {"User-Agent": "Python-App"}

    # Step 1: Get the list of files
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch API: {response.status_code}")

    files = response.json()
    if not files:
        raise Exception("No files found in the repository path.")

    # Step 2: Choose the last file in the list
    latest_file = files[-1]
    download_url = latest_file.get("download_url")
    file_name = latest_file.get("name")

    if not download_url:
        raise Exception("No download URL found for the latest file.")

    # Step 3: Check if file already exists
    if os.path.exists(file_name):
        print(f"File '{file_name}' already exists. Skipping download...")
    else:
        # Download the file
        print("please waitt... Downloading latest file")
        file_response = requests.get(download_url, headers=headers)
        if file_response.status_code != 200:
            raise Exception(f"Failed to download file: {file_response.status_code}")

        # Save the file locally
        with open(file_name, "wb") as f:
            f.write(file_response.content)

        print(f"Downloaded '{file_name}' successfully.")

    return file_name

def check_url_in_file(file_name, url_to_check):
    # Open the downloaded file and check if the URL exists
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if url_to_check in line:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{url_to_check} has been BLOCKED by Nawala")
                return
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{url_to_check} is safe")  # Optional

def main():
    print("Nawala URL Checker")
    url_input = input("Input The URL: ")
    latest_file = download_latest_file()
    check_url_in_file(latest_file, url_input)

if __name__ == "__main__":
    main()
