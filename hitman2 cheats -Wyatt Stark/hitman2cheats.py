import pymem
import sys

# --- Configuration ---
# Memory Addresses for Hitman 2 Ammo (as provided by you)
ICA19_AMMO_ADDRESS = 0x1A5A39310
HACKEL9S_AMMO_ADDRESS = 0x1A63FE2E0
HX7_AMMO_ADDRESS = 0x1B45515B0  
BARTOLI_SHOTGUN_AMMO_ADDRESS = 0x1A4564160
BARTOLI_75S_PISTOL_AMMO_ADDRESS = 0x19F2410A0 # Bartoli 75S Pistol re-added

GAME_PROCESS_NAME = "hitman2.exe"

# --- Main Script ---

try:
    pm = pymem.Pymem(GAME_PROCESS_NAME)
    print(f"Successfully attached to {GAME_PROCESS_NAME}")
except pymem.exception.PymemError:
    print(f"Error: Could not find or attach to the process '{GAME_PROCESS_NAME}'. Ensure the game is running.")
    sys.exit(1)

def modify_weapon_ammo(weapon_name, address):
    """
    Function to handle reading, prompting for input, and writing the new ammo value.
    """
    print(f"\n--- {weapon_name} Ammo Modifier ---")
    try:
        # Read current ammo
        current_ammo = pm.read_int(address)
        print(f"Current Ammo for {weapon_name}:", current_ammo)

        # Get user input for new ammo
        user_input = int(input(f"How much ammo do you need for the {weapon_name}? "))
        
        # Write new ammo
        pm.write_int(address, user_input)

        print(f"There's your ammo! Credits to Swedz for the code!!! New {weapon_name} Ammo:", user_input)

    except pymem.exception.MemoryReadError:
        print(f"Error reading memory at {weapon_name} address: {hex(address)}. Address may be invalid or outdated.")
    except pymem.exception.MemoryWriteError:
        print(f"Error writing memory at {weapon_name} address: {hex(address)}. Address may be invalid or outdated.")
    except ValueError:
        print(f"Invalid input for {weapon_name} ammo. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred during {weapon_name} modification: {e}")


# 🔫 Run Ammo Modifications for all five weapons
modify_weapon_ammo("ICA19", ICA19_AMMO_ADDRESS)
modify_weapon_ammo("Hackel 9S", HACKEL9S_AMMO_ADDRESS)
modify_weapon_ammo("Bartoli Shotgun", BARTOLI_SHOTGUN_AMMO_ADDRESS)
modify_weapon_ammo("Bartoli 75S Pistol", BARTOLI_75S_PISTOL_AMMO_ADDRESS) # Pistol re-added here
modify_weapon_ammo("HX-7", HX7_AMMO_ADDRESS)

# Script complete
print("\nAll requested ammo modifications completed.")