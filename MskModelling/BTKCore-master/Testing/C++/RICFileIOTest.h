#ifndef RICFileIOTest_h
#define RICFileIOTest_h

#include <btkRICFileIO.h>

CXXTEST_SUITE(RICFileIOTest)
{
  CXXTEST_TEST(Extensions)
  {
    btk::RICFileIO::Pointer pt = btk::RICFileIO::New();
    btk::RICFileIO::Extensions ext = pt->GetSupportedExtensions();
    TS_ASSERT_EQUALS(ext.GetSize(), 2);
  };
  
  CXXTEST_TEST(CanReadFileEmpty)
  {
    btk::RICFileIO::Pointer pt = btk::RICFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(""), false);
  };
  
  CXXTEST_TEST(CanReadFileFail)
  {
    btk::RICFileIO::Pointer pt = btk::RICFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(EliteFilePathIN + "Fail.ric"), false);
  };
  
  CXXTEST_TEST(CanReadFileOk)
  {
    btk::RICFileIO::Pointer pt = btk::RICFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(EliteFilePathIN + "1123xa01/1123xa01.RIC"), true);
  };
};

CXXTEST_SUITE_REGISTRATION(RICFileIOTest)
CXXTEST_TEST_REGISTRATION(RICFileIOTest, Extensions)
CXXTEST_TEST_REGISTRATION(RICFileIOTest, CanReadFileEmpty)
CXXTEST_TEST_REGISTRATION(RICFileIOTest, CanReadFileFail)
CXXTEST_TEST_REGISTRATION(RICFileIOTest, CanReadFileOk)
#endif
