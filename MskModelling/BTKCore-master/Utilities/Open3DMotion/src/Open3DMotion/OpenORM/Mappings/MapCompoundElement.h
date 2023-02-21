/*--
  Open3DMotion 
  Copyright (c) 2004-2012.
  All rights reserved.
  See LICENSE.txt for more information.
--*/

#ifndef _ORMPP_MAP_COMPOUND_ELEMENT_H_
#define _ORMPP_MAP_COMPOUND_ELEMENT_H_

#include "Open3DMotion/OpenORM/Mappings/MapElement.h"

namespace Open3DMotion
{
	class MapCompoundElement : public MapElement
	{
	public:
		MapCompoundElement(const char* _name);

		const char* Name() const
		{ return name; }

	private:
		const char* name;
	};

}
#endif