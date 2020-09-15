using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Reflection;
using System.Text;
using System.Xml.Linq;

namespace Shamped.Sword
{
    // http://dev.opml.org/spec2.html
    public class Opml
    {
        /*<head>*/

        [Category("head")]
        public string Title { get; set; }
        [Category("head")]
        public DateTime? DateCreated { get; set; }
        [Category("head")]
        public DateTime? DateModified { get; set; }
        [Category("head")]
        public string OwnerName { get; set; }
        [Category("head")]
        public string OwnerEmail { get; set; }
        [Category("head")]
        public string OwnerId { get; set; } //url
        [Category("head")]
        public string ExpansionState { get; set; } // 1, 6, 13, 16, 18, 20  or 1
        [Category("head")]
        public int? VertScrollState { get; set; }
        [Category("head")]
        public int? WindowTop { get; set; }
        [Category("head")]
        public int? WindowLeft { get; set; }
        [Category("head")]
        public int? WindowBottom { get; set; }
        [Category("head")]
        public int? WindowRight { get; set; }


        /*<body>*/
        [Category("body")]
        public List<Outline> Outlines { get; set; }
        public class Outline
        {
            [Category("outline")]
            public string Text { get; set; }
            [Category("outline")]
            public string Title { get; set; }
            [Category("outline")]
            public string Description { get; set; }
            [Category("outline")]
            public string Category { get; set; }
            [Category("outline")]
            public string Type { get; set; } //rss -htmlUrl xmlUrl,link - url,include - url
            [Category("outline")]
            public string Version { get; set; } //RSS2
            [Category("outline")]
            public string Language { get; set; }
            [Category("outline")]
            public string HtmlUrl { get; set; }
            [Category("outline")]
            public string XmlUrl { get; set; }
            [Category("outline")]
            public string Url { get; set; }
            [Category("outline")]
            public DateTime? Created { get; set; }

            public List<Outline> Outlines { get; set; }


        }

        public string Serialize()
        {
            return Serialize(Encoding.Unicode);
        }
        public string Serialize(Encoding encoding)
        {
            var doc = new XDocument(new XElement("opml"));
            doc.Root.Add(new XAttribute("version", "2.0"));

            var head_XE = new XElement("head");
            var thisType = this.GetType();
            foreach (var item in thisType.GetProperties())
            {
                var attr = item.GetCustomAttribute<CategoryAttribute>();
                if (attr != null && attr.Category == "head")
                {
                    var value = item.GetValue(this);
                    if (value != null && !string.IsNullOrWhiteSpace(value.ToString()))
                        head_XE.Add(new XElement(item.Name.FirstCharToLower(), value));
                }
            }
            doc.Root.Add(head_XE);

            var body_XE = new XElement("body");
            var outlineType = typeof(Outline);
            foreach (var outline in Outlines)
            {
                var outline_XE = new XElement("outline");
                foreach (var item in outlineType.GetProperties())
                {
                    var attr = item.GetCustomAttribute<CategoryAttribute>();
                    if (attr != null && attr.Category == "outline")
                    {
                        var value = item.GetValue(outline);
                        if (value!=null && !string.IsNullOrWhiteSpace(value.ToString()))
                            outline_XE.Add(new XAttribute(item.Name.FirstCharToLower(), value));
                    }
                }
                body_XE.Add(outline_XE);
            }

            doc.Root.Add(body_XE);

            // 输出;
            var builder = new StringBuilder();
            using (TextWriter writer = new OpmlStringWriter(builder, encoding))
                doc.Save(writer);
            return builder.ToString();
        }
        internal class OpmlStringWriter : StringWriter
        {
            private readonly Encoding encoding;

            public OpmlStringWriter(StringBuilder sb, Encoding encoding) : base(sb)
            {
                this.encoding = encoding;
            }

            public override Encoding Encoding => encoding;
        }

    }
}
