using System;
using System.Xml.Linq;

namespace Shamped.Sword
{
    public static class Extends
    {
        public static string FirstCharToLower(this string input)
        {
            if (String.IsNullOrEmpty(input))
                return input;
            return input.Substring(0, 1).ToLower() + input.Substring(1);
        }

      
        

    }
}
