#ifndef PipelineTest_h
#define PipelineTest_h

#include <btkDataObject.h>
#include <btkProcessObject.h>

class Source : public btk::DataObject
{
public:
  typedef btkSharedPtr<Source> Pointer;
  static Pointer New() {return Pointer(new Source());}; 
  int GetValue() {return this->m_Val;};
  void SetValue(int val)
  {
    this->m_Val = val;
    this->Modified();
  };
private:
  Source() {this->m_Val = 0;};
  int m_Val;
};

class Filter : public btk::ProcessObject
{
public:
  typedef btkSharedPtr<Filter> Pointer;
  typedef btkSharedPtr<const Filter> ConstPointer;
  static Pointer New() {return Pointer(new Filter());}; 
  void SetInc(int inc)
  {
    this->m_Inc = inc; 
    this->Modified();
  };
  Source::Pointer GetInput() {return this->GetInput(0);};
  void SetInput(Source::Pointer input) {this->SetNthInput(0, input);};
  Source::Pointer GetOutput() {return this->GetOutput(0);};
  
protected:
  Source::Pointer GetInput(int idx) {return static_pointer_cast<Source>(this->GetNthInput(idx));};
  Source::Pointer GetOutput(int idx) {return static_pointer_cast<Source>(this->GetNthOutput(idx));};
  virtual btk::DataObject::Pointer MakeOutput(int /* idx */)
  {
    return Source::New();
  };
  virtual void GenerateData()
  {
    this->GetOutput()->SetValue(this->GetInput(0)->GetValue() + this->m_Inc);
  };
  
private:
  Filter()
  : btk::ProcessObject()
  {
    this->SetInputNumber(1);
    this->SetOutputNumber(1);
    this->m_Inc = 1;
  };
  
  int m_Inc;
};

CXXTEST_SUITE(PipelineTest)
{
  CXXTEST_TEST(PipelineOne)
  {
    Source::Pointer src = Source::New();
    src->SetValue(5);
    Filter::Pointer incFilt = Filter::New();
    incFilt->SetInput(src);
    Source::Pointer res = incFilt->GetOutput();
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
    incFilt->SetInc(2);
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 7);
    incFilt->SetInput(res);
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 9);
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 11);
    incFilt->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 13);
  };
  
  CXXTEST_TEST(PipelineTwo)
  {
    Source::Pointer src = Source::New();
    src->SetValue(5);
    Filter::Pointer incFilt1 = Filter::New();
    incFilt1->SetInput(src);
    Source::Pointer res1 = incFilt1->GetOutput();
    Filter::Pointer incFilt2 = Filter::New();
    incFilt2->SetInput(incFilt1->GetOutput());
    Source::Pointer res2 = incFilt2->GetOutput();
    res2->Update();
    TS_ASSERT_EQUALS(res1->GetValue(), 6);
    TS_ASSERT_EQUALS(res2->GetValue(), 7);
    incFilt2->SetInc(2);
    res2->Update();
    TS_ASSERT_EQUALS(res1->GetValue(), 6);
    TS_ASSERT_EQUALS(res2->GetValue(), 8);
  };
  
  CXXTEST_TEST(PipelineThree)
  {
    Source::Pointer src = Source::New();
    src->SetValue(5);
    Filter::Pointer incFilt = Filter::New();
    incFilt->SetInput(src);
    Source::Pointer res = incFilt->GetOutput();
    res->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
    res->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
    src->SetValue(6);
    res->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 7);
  };
  
  CXXTEST_TEST(DeleteParent)
  {
    Source::Pointer src = Source::New();
    src->SetValue(5);
    Filter::Pointer incFilt = Filter::New();
    incFilt->SetInput(src);
    Source::Pointer res = incFilt->GetOutput();
    res->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
    src->SetValue(6);
    incFilt.reset();
    res->Update();
    TS_ASSERT_EQUALS(res->GetValue(), 6);
  };
  
  CXXTEST_TEST(NewInput)
  {
    Source::Pointer src = Source::New();
    src->SetValue(5);
    Filter::Pointer incFilt1 = Filter::New();
    incFilt1->SetInput(src);
    Source::Pointer res1 = incFilt1->GetOutput();
    Filter::Pointer incFilt2 = Filter::New();
    incFilt2->SetInput(incFilt1->GetOutput());
    Source::Pointer res2 = incFilt2->GetOutput();
    res2->Update();
    Source::Pointer src2 = Source::New();
    incFilt1->SetInput(src2);
    res2->Update();
    TS_ASSERT_EQUALS(res1->GetValue(), 1);
    TS_ASSERT_EQUALS(res2->GetValue(), 2);
    Source::Pointer src3 = Source::New();
    src3->SetValue(5);
    incFilt1->SetInput(src3);
    res2->Update();
    TS_ASSERT_EQUALS(res1->GetValue(), 6);
    TS_ASSERT_EQUALS(res2->GetValue(), 7);
    Source::Pointer src4 = Source::New();
    src4->SetValue(10);
    incFilt1->SetInput(src4);
    incFilt2->SetInc(2);
    res2->Update();
    TS_ASSERT_EQUALS(res1->GetValue(), 11);
    TS_ASSERT_EQUALS(res2->GetValue(), 13);
  };
};

CXXTEST_SUITE_REGISTRATION(PipelineTest)
CXXTEST_TEST_REGISTRATION(PipelineTest, PipelineOne)
CXXTEST_TEST_REGISTRATION(PipelineTest, PipelineTwo)
CXXTEST_TEST_REGISTRATION(PipelineTest, PipelineThree)
CXXTEST_TEST_REGISTRATION(PipelineTest, DeleteParent)
CXXTEST_TEST_REGISTRATION(PipelineTest, NewInput)
#endif
