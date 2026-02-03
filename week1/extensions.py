extens = input("File name:").lower().strip()
if extens.endswith("jpg") or extens.endswith("jpeg"):
    print("image/jpeg")
elif extens.endswith("pdf"):
    print("application/pdf")
elif extens.endswith("gif"):
    print("image/gif")
elif extens.endswith("png"):
    print("image/png")
elif extens.endswith("txt"):
    print("text/plain")
elif extens.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")


