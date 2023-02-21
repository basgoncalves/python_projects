/*--
  Open3DMotion 
  Copyright (c) 2004-2012.
  All rights reserved.
  See LICENSE.txt for more information.
--*/

#include "Open3DMotion/Biomechanics/Trial/EventNameID.h"

namespace Open3DMotion
{
	EventNameID::EventNameID()
	{
		REGISTER_MEMBER(Name);
		REGISTER_MEMBER(ID);
	}
}
