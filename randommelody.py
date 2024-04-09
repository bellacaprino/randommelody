from mido import Message, MidiFile, MidiTrack
import random

def generate_random_melody(note_count, filename):
    # Define the range of MIDI note numbers for the melody
    note_range_start = 48  # C3
    note_range_end = 84    # C6
    
    # Generate a random melody
    random_melody = [random.randint(note_range_start, note_range_end) for _ in range(note_count)]
    
    # Create a new MIDI file and track
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)
    
    # Add notes to the track
    for note in random_melody:
        # Note on
        track.append(Message('note_on', note=note, velocity=64, time=0))
        # Note off after 480 ticks (default tempo, quarter note = 480 ticks)
        track.append(Message('note_off', note=note, velocity=64, time=480))
    
    # Save the MIDI file
    midi_file.save(filename)
    
    return random_melody, filename

# Settings
note_count = 5  # Number of notes you want in the melody
midi_filename = "random_melody.mid"  # MIDI file output location

# Generate the melody and MIDI file
melody, filename = generate_random_melody(note_count, midi_filename)

print("Generated Melody:", melody)
print("MIDI file saved as:", filename)

