// FILE: prog4.cpp
// J. Hall, Transy U
// CS 2124, Winter 2022
//
//  Sort a list of Olympic teams into decreasing order by number of athletes
//        into incremental bus departures and display the bus schedule
//                       after input is received
//

#include <iostream>
#include <fstream>
using namespace std;
const int MAX_TEAMS = 385;
const int MAX_BUSES = 7;
const int MAX_TEAMS_PER_BUS = 55;
const int BUSES_GONE_BY_130PM = 2;
const int BUSES_GONE_BY_230PM = 4;
const int BUSES_GONE_BY_330PM = 6;

// new data types
struct Team {
    int athletes;
    string sport;
    string country;
};

struct Bus {
    int busNumber;
    int riders;
    int teamCount;
    int departureHour;
    string departureMins;
    Team teamsOnBus[MAX_TEAMS_PER_BUS];
};

// function prototypes
void initBuses(Bus bs[], int MAX_BUSES);
int readTeams(ifstream& tFile, Team ts[]);
void readTeam(ifstream& tFile, Team& t);
void sortTeamsBySize(Team ts[], int tCount);
void swapTeams(Team& t0, Team& t1);
void loadTeamsOntoBuses(Team ts[], int tCount, Bus bs[]);
void loadTeamOntoSomeBus(Team t, Bus bss[]);
void departHour(Bus bs[]);
void departMins(Bus bs[]);
void printBuses(ostream& bFile, Bus bs[]);
void printTeam(ostream& bFile, Team t);

// main program
int main(void){
    ifstream teamInputFile;
    ofstream busOutputFile;
    int tCount;
    Team teams[MAX_TEAMS];
    Bus buses[MAX_BUSES];

// title
    cout << endl << "\t\t\t\tFIRST FIT DECREASING BIN PACKING ALGORITHM"
         << endl << endl << endl;

// initialize the array of Bus structures
    initBuses(buses, MAX_BUSES);

// read a list of teams
//// open input file for reading
    teamInputFile.open("p4in.txt");
    if (!teamInputFile) {
        cout << "\t\tERROR! Input File not in same folder as rest of program.";
        exit(1);
    }

//// read number of teams and each team's information from input file
    tCount = readTeams(teamInputFile, teams);
    teamInputFile.close();


// open an output file for writing
    busOutputFile.open("p4out.txt");
    if (!busOutputFile) {
        cout << "\t\tERROR! Output File cannot be written to.";
    }

// sort teams by size
    sortTeamsBySize(teams, tCount);

// load each team into buses
    loadTeamsOntoBuses(teams, tCount, buses);

// schedule departure time for each bus
    departHour(buses);
    departMins(buses);

// print out list of bus information to output file
    printBuses(busOutputFile, buses);
    busOutputFile.close();

// print out list of bus information to screen
    printBuses(cout, buses);

    return 0;
}



// functions //

    // initBuses fn
    //// set number of riders and teams in buses array to zero
    void initBuses(Bus bs[], int MAX_BUSES){
        for (int i = 0; i < MAX_BUSES; i++) {
            bs[i].riders = 0;
            bs[i].teamCount = 0;
        }
    }


    // readTeams fn
    int readTeams(ifstream& tFile, Team ts[]) {

    //// read number of teams
        int tCount;
        tFile >> tCount;

    //// read information for teams
        for (int i = 0; i < tCount; i++) {
            readTeam(tFile, ts[i]);
        }
        return tCount;
    }


    // readTeam fn
    //// assign inputs from file to information in a Team structure
    void readTeam(ifstream& tFile, Team& t){
        tFile >> t.athletes;
        tFile >> t.sport;
        tFile >> t.country;
    }


    // sortTeamsBySize fn
    //// sorts teams in decreasing order of size
    void sortTeamsBySize(Team ts[], int tCount) {
    int tPairs = (tCount - 1);
    bool swapFlag;

    //// swap order of array pair if next value in pair bigger than previous
    do{
        swapFlag = false;
        for (int i = 0; i < tPairs; i++){
            if (ts[i].athletes < ts[i+1].athletes) {
                swapTeams(ts[i], ts[i+1]);
                swapFlag = true;
            }
        }
    }while (swapFlag);
}


    // swapTeams fn
    //// swaps order of elements in an array
    void swapTeams(Team& t0, Team& t1){
        Team tempTeam;
        tempTeam = t0;
        t0 = t1;
        t1 = tempTeam;
    }


    // loadTeamsOntoBuses fn
    //// loads a list of teams onto buses
    void loadTeamsOntoBuses(Team ts[], int tCount, Bus bs[]) {
        for (int i = 0; i < tCount; i++) {
            loadTeamOntoSomeBus(ts[i], bs);
        }
    }


    // loadTeamOntoSomeBus fn
    //// ensures maximized space used in each bus for most efficient transport
    void loadTeamOntoSomeBus(Team t, Bus bss[]) {
        int busIndex = 0;
        do {

    //// if the next largest Team structure in list fits into the first available bus, place structure into Bus structure
            if (t.athletes <= (MAX_TEAMS_PER_BUS - bss[busIndex].riders)){
                bss[busIndex].riders = (bss[busIndex].riders + t.athletes);
                int teamIndex = bss[busIndex].teamCount;
                bss[busIndex].teamsOnBus[teamIndex] = t;
                bss[busIndex].teamCount = (bss[busIndex].teamCount + 1);
                bss[busIndex].busNumber = (busIndex + 1);

    //// leave loop if team has been added to a bus
                break;
            }

    //// otherwise move on to next available bus and begin loop again to see if next team will fit, until one does
            else {
                busIndex++;
            }
        } while (true);
    }


    // departHour fn
    void departHour(Bus bs[]) {
        for (int i = 0; i < MAX_BUSES; i++) {

    //// set first two buses to leave after 1:00 and before 2:00
            if (i < BUSES_GONE_BY_130PM){
                bs[i].departureHour = 1;
            }

    //// set next two buses in array to leave at 2:00 or before 3:00 (if necessary)
            if ((BUSES_GONE_BY_130PM <= i) && (i < BUSES_GONE_BY_230PM)) {
                bs[i].departureHour = 2;
            }

    //// set next two buses in array to leave at 3:00 or before 4:00 (if necessary)
            if ((BUSES_GONE_BY_230PM <= i) && (i < BUSES_GONE_BY_330PM)) {
                bs[i].departureHour = 3;
            }
    //// set last bus to leave at 4:00 (if necessary)
            if (i == MAX_BUSES) {
                bs[i].departureHour = 4;
            }
        }
    }


    // departMins fn
    void departMins(Bus bs[]) {

    //// if index in array is even, they'll be leaving on the hour
        for (int i = 0; i < MAX_BUSES; i++) {
            if ((i == 0) || (i == BUSES_GONE_BY_130PM) || (i == BUSES_GONE_BY_230PM) || (i == BUSES_GONE_BY_330PM)) {
                bs[i].departureMins = "00";
            }

    //// if index in array is odd, they'll be leaving at half hour mark
            else {
            bs[i].departureMins = "30";
            }
        }
    }

    // printBuses fn
    //// print a list of buses' information
    void printBuses(ostream& bFile, Bus bs[]){
        int busIndex = 0;

    //// print information as long as there is at least one team in the bus
        while (bs[busIndex].teamCount != 0) {
            bFile << "Bus " << bs[busIndex].busNumber << " leaves at "
                  << bs[busIndex].departureHour << ":" << bs[busIndex].departureMins
                  << "pm with " << bs[busIndex].riders << " passengers:" << endl;
            for (int i = 0; i < bs[busIndex].teamCount; i++) {
                printTeam(bFile, bs[busIndex].teamsOnBus[i]);
            }
            busIndex++;
        }
    }


    // printTeam fn
    //// print information for one team on the bus
    void printTeam(ostream& bFile, Team t) {
        bFile << "\t" << t.athletes << " athletes from "
              << t.country << "'s " << t.sport << " team" <<endl;
    }
