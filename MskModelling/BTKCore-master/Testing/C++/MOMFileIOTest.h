#ifndef MOMFileIOTest_h
#define MOMFileIOTest_h

#include <btkMOMFileIO.h>

CXXTEST_SUITE(MOMFileIOTest)
{
  CXXTEST_TEST(CanReadFileEmpty)
  {
    btk::MOMFileIO::Pointer pt = btk::MOMFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(""), false);
  };
  
  CXXTEST_TEST(CanReadFileFail)
  {
    btk::MOMFileIO::Pointer pt = btk::MOMFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(EliteFilePathIN + "Fail.mom"), false);
  };
  
  CXXTEST_TEST(CanReadFileOk)
  {
    btk::MOMFileIO::Pointer pt = btk::MOMFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(EliteFilePathIN + "1123xa01/1123xa01.MOM"), true);
  };
};

CXXTEST_SUITE_REGISTRATION(MOMFileIOTest)
CXXTEST_TEST_REGISTRATION(MOMFileIOTest, CanReadFileEmpty)
CXXTEST_TEST_REGISTRATION(MOMFileIOTest, CanReadFileFail)
CXXTEST_TEST_REGISTRATION(MOMFileIOTest, CanReadFileOk)
#endif
