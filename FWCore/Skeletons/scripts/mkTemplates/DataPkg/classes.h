#include "DataFormats/Common/interface/Wrapper.h"

//Add includes for your classes here
#include "skelsubsys/datapkgname/interface/YOUR_CLASS_GOES_HERE.h"
#include <vector>

namespace {
   struct skelsubsys_datapkgname {
      //add 'dummy' Wrapper variable for each class type you put into the Event
      edm::Wrapper<YOUR_CLASS_GOES_HERE> dummy1;
      std::vector<YOUR_CLASS_GOES_HERE> dummy2;
      edm::Wrapper<std::vector<YOUR_CLASS_GOES_HERE> > dummy3;
/*
    These classes are commented out because they are used more rarely. If you need them, move them
    outside the comments and make the corresponding change in classes_def.xml
      
uncomment_h_here

      edm::Ref<std::vector<YOUR_CLASS_GOES_HERE> > dummy4;
      edm::RefVector<std::vector<YOUR_CLASS_GOES_HERE> > dummy5;
      edm::RefProd<std::vector<YOUR_CLASS_GOES_HERE> > dummy6;
*/

   };
}
