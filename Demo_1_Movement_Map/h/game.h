/*
 * This file is part of the Marmalade SDK Code Samples.
 *
 * (C) 2001-2012 Marmalade. All Rights Reserved.
 *
 * This source code is intended only as a supplement to the Marmalade SDK.
 *
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
 * KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 * PARTICULAR PURPOSE.
 */
#ifndef GAME_H
#define GAME_H
#include "map.h"
#include "character.h"
#include "tile.h"
class CGame
{
public:
    CGame();
    ~CGame();

    // update will be called a fixed number of times per second
    // regardless of visual framerate
    void Update(int deltaTime);
    // render will be called as fast as possible (but not faster
    // than the update rate)
    void Render();

	// loading images from resource
	void LoadRes();
private:
	Map* m_Map;
	Character* m_Character;
	Tile* m_Tile;
};

#endif
