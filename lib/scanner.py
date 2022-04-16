def urlscan(url):
  parts = url.split("/")
  return parts[3], parts[4]
