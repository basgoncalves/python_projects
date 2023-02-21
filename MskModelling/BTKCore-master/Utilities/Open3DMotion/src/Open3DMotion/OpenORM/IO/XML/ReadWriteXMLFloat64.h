/*--
  Open3DMotion 
  Copyright (c) 2004-2012.
  All rights reserved.
  See LICENSE.txt for more information.
--*/

#ifndef _READ_WRITE_XML_FLOAT64_H_
#define _READ_WRITE_XML_FLOAT64_H_

#include "ReadWriteXML.h"
#include "Open3DMotion/OpenORM/Leaves/TreeFloat64.h"

namespace Open3DMotion
{
	class ReadWriteXMLFloat64 : public ReadWriteXML
	{
	public:
		virtual const char* TypeAttribute() const
		{ return "double"; }

		virtual const char* SupportedValueClass() const
		{ return TreeFloat64::classname; }

		virtual void WriteValue(XMLWritingMachine& writer, const TreeValue* value) const;

		virtual TreeValue* ReadValue(XMLReadingMachine& reader, const pugi::xml_node& element) const;
	};
}

#endif
