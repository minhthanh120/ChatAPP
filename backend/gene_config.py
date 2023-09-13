import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("URLBackend")
# ADD SETTINGS TO SECTION
config_file.set("URLBackend", "Url", "127.0.0.1")
config_file.set("URLBackend", "Port", "8089")

# ADD SECTION
config_file.add_section("ConnectionString")
# ADD SETTINGS TO SECTION
config_file.set("ConnectionString", "EngineUrl",YOUR_CONNECTRING_HERE)

# SAVE CONFIG FILE
with open(r"config.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'config.ini' created")

# PRINT FILE CONTENT
read_file = open("config.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()