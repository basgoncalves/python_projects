#ifndef TDFFileIOTest_h
#define TDFFileIOTest_h

#include <btkTDFFileIO.h>

CXXTEST_SUITE(TDFFileIOTest)
{
  CXXTEST_TEST(AvailableOperations)
  {
    TS_ASSERT_EQUALS(btk::TDFFileIO::HasReadOperation(), true);
    TS_ASSERT_EQUALS(btk::TDFFileIO::HasWriteOperation(), false);
  };
  
  CXXTEST_TEST(CanReadFileEmpty)
  {
    btk::TDFFileIO::Pointer pt = btk::TDFFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(""), false);
  };
  
  CXXTEST_TEST(CanReadFileEmptyFile)
  {
    btk::TDFFileIO::Pointer pt = btk::TDFFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(TDFFilePathIN + "empty.tdf"), false);
  };
  
  CXXTEST_TEST(CanReadFileFail)
  {
    btk::TDFFileIO::Pointer pt = btk::TDFFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(TDFFilePathIN + "False.tdf"), false);
  };
  
  CXXTEST_TEST(CanReadFileOk)
  {
    btk::TDFFileIO::Pointer pt = btk::TDFFileIO::New();
    TS_ASSERT_EQUALS(pt->CanReadFile(TDFFilePathIN + "gait9.tdf"), true);
  };
};

CXXTEST_SUITE_REGISTRATION(TDFFileIOTest)
CXXTEST_TEST_REGISTRATION(TDFFileIOTest, AvailableOperations)
CXXTEST_TEST_REGISTRATION(TDFFileIOTest, CanReadFileEmpty)
CXXTEST_TEST_REGISTRATION(TDFFileIOTest, CanReadFileEmptyFile)
CXXTEST_TEST_REGISTRATION(TDFFileIOTest, CanReadFileFail)
CXXTEST_TEST_REGISTRATION(TDFFileIOTest, CanReadFileOk)
#endif
