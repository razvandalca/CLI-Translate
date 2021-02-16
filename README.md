# cli-translate-app

## Getting started
1. Install Docker Community Edition.
2. Go into the docker folder
	```
	cd docker
	```
3. Build-up and launch the environment.
    ```
	docker-compose up --build 
    ```
4. Connect to container
    ```
    docker exec -it cli-app bash
    ```
5. Start using gtranslate. You have a txt file with some text. You can update directly the file and it will update in container. This is just for convenience. 
     ```
    root@319bd4c6b12b:/app# gtranslate translate -f input-example.txt -l de
    Guten Morgen
    Guten Abend
    Boy Tag
    Bis später
    Gesundheit
     ```
   
6. The command available is translate. For more info use --h 
     ```
    root@319bd4c6b12b:/app# gtranslate translate --h
    usage: gtranslate translate [-h] [-f FILE] [-l LANGUAGE]
                                [--fullOutput FULLOUTPUT]
    
    A command to translate a text file to a specific language
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  path to input file to be translated
      -l LANGUAGE, --language LANGUAGE output language, can be one of "en", "it" or "de"
      --fullOutput FULLOUTPUT Show full data after translation
  ```
