#ifndef SE_H
#define SE_H
//#include "audio.h"
#include "s3e.h"
#include "IwSound.h"
class SE
{
public:
	SE(){};
	~SE(){};
	void Stop();
	void Pause();
	void Resume();
	bool Update(bool play);
	void Play();
	void Init(char* filename1,char* filename2);
	CIwSoundInst* _soundInstance1;
	CIwSoundInst* _soundInstance2;
	CIwSoundSpec* _soundSpec1;
	CIwSoundSpec* _soundSpec2;
	int lastPlayed;
private:
	bool _Play;
	//CIwSoundSpec* _soundSpec;
};
#endif