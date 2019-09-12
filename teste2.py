registro = open('acessos.log', 'r')
sites_sem_https = [url for url in registro if url.startswith('http://')]

print(sites_sem_https[1])