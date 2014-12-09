# Team Tigris - Carleton tunnel traffic monitor
### Sends Tweet for the deployed tunnel zone (through device agnosticism principles, nodes can be made to span the entire tunnel network)
> An indoor traffic monitor using two human sensing methods, three Raspberry Pis and two gertboards; Project requirement was to use Three Raspberry Pis, one with gertboard and the other with PiFace but our PiFace was damaged.

## Quick start
- Clone this repository

```bash
$ git clone https://github.com/bhargavrpatel/SYSC-3010---Team-Tigris---Final-Project.git
```

- Hook up the equipment

- Run gertv4 on I/O connected Pis.

- Run heartv4 on Twitter related Pi


## Testing
- Run two instances of boilerplateGERT.py with differnt port addresses

```bash
$ sudo python3 boilerplateGERT.py 7600
$ sudo python3 boilerplateGERT.py 10000
```

- Change the array within setUP() method in test_heartv4.py with the chosen ports

- Run the test_heartv4.py 
