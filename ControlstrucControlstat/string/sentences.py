subs = ['I','You']
verbs = ['play','love']
subjs = ['cricket','football']
print '\n'.join([sub+' '+verb+' '+subj for sub in subs for verb in verbs for subj in subjs])
