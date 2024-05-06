// FILE: parkngLotTracker
// J Hall, Transy U
// CS 2124, Winter 2022
//
// This program takes in vehicle information from the user to simulate
// the tracking of reserved valet parking spots for two different sports teams.
//
#include <iostream>

using namespace std;

// symbolic constants
const int MAX_TEAM_SPOTS = 5;
const int TOT_SPOTS = 10;

// new data types
struct Park {
    string lName;
    string lPlate;
};

// main program
int main(void) {
    Park beng[MAX_TEAM_SPOTS], ram[MAX_TEAM_SPOTS];
    int bSpotsTaken, rSpotsTaken;
    string lastName, licPlate, team;

//// title
    cout << endl << "\t\t SUPER BOWL VIP VALET REGISTER"
         << endl;

//// assign variables to 0
    bSpotsTaken = 0;
    rSpotsTaken = 0;

//// begin loop for prompt and storing of data until both teams' spots are full
    while ((bSpotsTaken < MAX_TEAM_SPOTS) || (rSpotsTaken < MAX_TEAM_SPOTS)) {
        cout << endl << "  Most Recent Parked Vehicle's Information:"
             << endl;
        cout << "\tLast Name: ";
        cin >> lastName;

////// ends prompts if sentinel LVI is entered
            if (lastName == "LVI") {
                break;
            }

////// continue otherwise
            else {
                cout << "\tLicense Plate: ";
                cin >> licPlate;
                cout << "\tTeam Initial [B or R]: ";
                cin >> team;
            }

////// if Bengals spots are full, print error message. if not, assign values to array
        if ((team == "B") || (team == "b")) {
            if (bSpotsTaken >= MAX_TEAM_SPOTS) {
                cout << endl << "\tSorry! No spots remaining for the Bengals."
                     << endl;
            }
            else {
                beng[bSpotsTaken].lName = lastName;
                beng[bSpotsTaken].lPlate = licPlate;
                bSpotsTaken = ++bSpotsTaken;
            }
        }

////// if Rams spots are full, print error message. if not, assign values to array
        else
            if (rSpotsTaken >= MAX_TEAM_SPOTS) {
                cout << endl << "\tSorry! No spots remaining for the Rams."
                     << endl;
            }

            else {
                ram[rSpotsTaken].lName = lastName;
                ram[rSpotsTaken].lPlate = licPlate;
                rSpotsTaken = ++rSpotsTaken;
            }
    }

//// print the valet summary report
////// title
    cout << endl << endl << endl
         << "  VALET RECORD:" << endl;

////// Bengals info title
    cout << "\tBengals:" << endl;

////// print message if no parking spots taken by Bengals
    if (bSpotsTaken == 0) {
        cout << "\t\tThere are no Bengals VIP vehicles parked in the Ultra Elite Lot."
             << endl;
    }

////// begin loop to print each slot's information for the Bengals
    else {
        for (int s = 0; s < bSpotsTaken; ++s) {
            cout << "\t\tSpot:  " << (s + 1) << "00"
                 << "\t\tLast Name:  " << beng[s].lName
                 << "\t\t\tLicense Plate:  " << beng[s].lPlate
                << endl;
        }
    }

////// Rams info title
    cout << endl << "\tRams:"
         << endl;

////// print message if no parking spots taken by Rams
    if (rSpotsTaken == 0) {
        cout << "\t\tThere are no Rams VIP vehicles parked in the Ultra Elite Lot."
             << endl;
    }

////// begin loop to print each spot's information for the Rams
     else {
        for (int s = 0; s < rSpotsTaken; ++s) {
            cout << "\t\tSpot:  " << (s + 1) << "00"
                 << "\t\tLast Name:  " << ram[s].lName
                 << "\t\t\tLicense Plate:  " << ram[s].lPlate
                 << endl;
        }
     }

// end program
    return 0;
}
