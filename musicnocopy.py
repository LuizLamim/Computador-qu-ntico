from midiutil import MIDIFile

# Configurações da Faixa
degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # Escala de Dó Maior
track    = 0
channel  = 0
time     = 0    # Começo da música
duration = 1    # Duração de cada nota
tempo    = 128  # BPM (128 é clássico para música eletrônica/viral)
volume   = 100  # 0-127

# Cria o objeto MIDI com 2 trilhas (Melodia e Bateria/Baixo)
MyMIDI = MIDIFile(2)

# --- TRILHA 1: Melodia (Loop cativante) ---
MyMIDI.addTrackName(0, time, "Melodia Viral")
MyMIDI.addTempo(0, time, tempo)

# Uma progressão simples e feliz (I - V - vi - IV)
# Notas MIDI: C4=60, G3=55, A3=57, F3=53
progression_notes = [60, 67, 69, 65, 60, 67, 69, 72] 
times = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5] # Ritmo rápido

# Repetir o loop por 8 compassos
for i in range(8):
    base_time = i * 4
    for note, t in zip(progression_notes, times):
        MyMIDI.addNote(0, channel, note, base_time + t, 0.5, volume)

# --- TRILHA 2: Batida Base (Kick simples) ---
MyMIDI.addTrackName(1, time, "Beat")
MyMIDI.addTempo(1, time, tempo)

# Batida "Four on the floor" (típica de música viral)
for i in range(32): # 32 batidas
    MyMIDI.addNote(1, 9, 36, i, 1, 110) # 36 é o Kick Drum no canal 10 (GM standard, aqui simulado no 9)

# Salvar o arquivo
with open("minha_musica_viral.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

print("Arquivo 'minha_musica_viral.mid' gerado com sucesso!")