/*--
  Open3DMotion 
  Copyright (c) 2004-2012.
  All rights reserved.
  See LICENSE.txt for more information.
--*/

#ifndef _ORMPP_TREE_BOOL_H_
#define _ORMPP_TREE_BOOL_H_

#include "Open3DMotion/OpenORM/Leaves/TreeSimpleValue.h"

namespace Open3DMotion
{
	class TreeBool : public TreeSimpleValue<bool>
	{
	public:				
		DECLARE_CLASS_NAME();

		TreeBool(bool _x = false);

		virtual TreeBool* NewBlank() const;
	};
}
#endif